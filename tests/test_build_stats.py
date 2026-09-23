import importlib.util
import io
import pathlib
import unittest
import urllib.error
from unittest import mock


SCRIPT = pathlib.Path(__file__).parents[1] / "scripts" / "build_stats.py"
SPEC = importlib.util.spec_from_file_location("build_stats", SCRIPT)
build_stats = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(build_stats)


def repo(repo_id, *, owner="Caden-1224", fork=False, private=False, stars=0):
    return {
        "id": repo_id,
        "owner": {"login": owner},
        "fork": fork,
        "private": private,
        "stargazers_count": stars,
    }


class CollectTests(unittest.TestCase):
    def test_collect_filters_scope_and_deduplicates_moving_pages(self):
        first_page = [repo(i, stars=1) for i in range(1, 101)]
        # The duplicate models a repository moving across pages while the API
        # is being read. The final page contains all excluded repository kinds.
        second_page = [
            first_page[0],
            repo(101, fork=True, stars=100),
            repo(102, private=True, stars=100),
            repo(103, owner="someone-else", stars=100),
        ]

        def fake_rest(path):
            if path.endswith("page=1"):
                return mock.Mock(), first_page
            if path.endswith("page=2"):
                return mock.Mock(), second_page
            self.fail("unexpected API path: " + path)

        with mock.patch.object(build_stats, "rest", new=mock.Mock(side_effect=fake_rest)) as rest_mock:
            stats = build_stats.collect()

        self.assertEqual(stats["repos"], 100)
        self.assertEqual(stats["stars"], 100)
        self.assertEqual(rest_mock.call_count, 2)

    def test_collect_handles_short_first_page(self):
        page = [repo(1, stars=4)]
        with mock.patch.object(build_stats, "rest", return_value=(mock.Mock(), page)):
            stats = build_stats.collect()
        self.assertEqual(stats, {"login": "Caden-1224", "stars": 4, "repos": 1})

    def test_malformed_repository_does_not_publish_false_zero(self):
        for field, bad_value in (("stargazers_count", "4"), ("stargazers_count", -1),
                                 ("fork", None), ("owner", {}), ("id", None)):
            with self.subTest(field=field, value=bad_value):
                invalid = repo(1, stars=4)
                invalid[field] = bad_value
                with mock.patch.object(build_stats, "rest", return_value=(None, [invalid])):
                    with self.assertRaises(ValueError):
                        build_stats.collect()

    def test_failed_second_page_does_not_return_partial_totals(self):
        with mock.patch.object(build_stats, "rest", side_effect=[
            (None, [repo(i) for i in range(100)]), urllib.error.URLError("offline")
        ]):
            with self.assertRaises(urllib.error.URLError):
                build_stats.collect()


class RequestTests(unittest.TestCase):
    def test_public_api_works_without_authorization_header(self):
        with mock.patch.object(build_stats, "TOKEN", None), mock.patch.object(
            build_stats.urllib.request, "urlopen", return_value=io.BytesIO(b"[]")
        ) as request:
            _, result = build_stats.rest("/users/test/repos")
        self.assertEqual(result, [])
        self.assertIsNone(request.call_args.args[0].get_header("Authorization"))

    def test_transient_server_error_retries(self):
        unavailable = urllib.error.HTTPError("url", 503, "unavailable", {}, None)
        with mock.patch.object(build_stats.urllib.request, "urlopen", side_effect=[
            unavailable, io.BytesIO(b"[]")
        ]) as request, mock.patch.object(build_stats.time, "sleep") as sleep:
            _, result = build_stats.rest("/users/test/repos")
        self.assertEqual(result, [])
        self.assertEqual(request.call_count, 2)
        sleep.assert_called_once_with(1)

    def test_primary_rate_limit_fails_without_retries_or_fake_data(self):
        limited = urllib.error.HTTPError("url", 403, "rate limit", {"X-RateLimit-Remaining": "0"}, None)
        with mock.patch.object(build_stats.urllib.request, "urlopen", side_effect=limited) as request:
            with self.assertRaises(urllib.error.HTTPError):
                build_stats.rest("/users/test/repos")
        self.assertEqual(request.call_count, 1)

    def test_secondary_rate_limit_honors_retry_after(self):
        limited = urllib.error.HTTPError("url", 403, "rate limit", {"Retry-After": "2"}, None)
        with mock.patch.object(build_stats.urllib.request, "urlopen", side_effect=[
            limited, io.BytesIO(b"[]")
        ]), mock.patch.object(build_stats.time, "sleep") as sleep:
            build_stats.rest("/users/test/repos")
        sleep.assert_called_once_with(2)

    def test_long_retry_after_fails_without_retrying_early(self):
        limited = urllib.error.HTTPError("url", 429, "rate limit", {"Retry-After": "60"}, None)
        with mock.patch.object(build_stats.urllib.request, "urlopen", side_effect=limited) as request, mock.patch.object(build_stats.time, "sleep") as sleep:
            with self.assertRaises(urllib.error.HTTPError):
                build_stats.rest("/users/test/repos")
        self.assertEqual(request.call_count, 1)
        sleep.assert_not_called()

    def test_network_failure_stops_after_bounded_attempts(self):
        with mock.patch.object(build_stats.urllib.request, "urlopen", side_effect=urllib.error.URLError("offline")) as request, mock.patch.object(build_stats.time, "sleep"):
            with self.assertRaises(urllib.error.URLError):
                build_stats.rest("/users/test/repos")
        self.assertEqual(request.call_count, build_stats.MAX_ATTEMPTS)


class RenderingTests(unittest.TestCase):
    def test_card_describes_public_scope_and_escapes_text(self):
        svg = build_stats.card(
            {"login": "A<&", "stars": 1234, "repos": 7}, build_stats.LIGHT, "2026-09-24T14:17Z"
        )
        self.assertIn("1,234", svg)
        self.assertIn("owned public non-fork repositories", svg)
        self.assertIn("UPDATED 09-24 14:17 UTC", svg)
        self.assertIn("Last successful update: 2026-09-24T14:17Z", svg)
        self.assertNotIn("TOTAL COMMITS", svg)
        self.assertIn("A&lt;&amp;", svg)

    def test_updated_date_rejects_ambiguous_input(self):
        with mock.patch.dict(build_stats.os.environ, {"STATS_DATE": "yesterday"}, clear=False):
            with self.assertRaises(ValueError):
                build_stats._updated_date()


if __name__ == "__main__":
    unittest.main()
