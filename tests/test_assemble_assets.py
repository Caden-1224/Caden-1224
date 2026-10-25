import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

SCRIPT = Path(__file__).parents[1] / "scripts" / "assemble_assets.py"
SPEC = importlib.util.spec_from_file_location("assemble_assets", SCRIPT)
assets = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(assets)


def write_pair(directory, kind, label):
    directory.mkdir(parents=True, exist_ok=True)
    for name in assets.PAIRS[kind]:
        (directory / name).write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg"><text>{label}</text></svg>', encoding="utf-8"
        )


class AssemblyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.previous = self.root / "previous"
        self.stats = self.root / "stats-next"
        self.snake = self.root / "snake-next"
        self.output = self.root / "dist"
        self.log = contextlib.redirect_stdout(io.StringIO())
        self.log.__enter__()
        self.addCleanup(self.log.__exit__, None, None, None)

    def assemble(self, stats_ok=True, snake_ok=True):
        return assets.assemble(self.previous, self.stats, self.snake, self.output, stats_ok, snake_ok)

    def test_complete_new_pairs_publish_on_first_run(self):
        write_pair(self.stats, "stats", "new stats")
        write_pair(self.snake, "snake", "new snake")
        self.assertEqual(self.assemble(), {"can_publish": True, "degraded": False})
        self.assertEqual(len(list(self.output.iterdir())), 4)

    def test_failed_generator_cannot_replace_old_pair_with_partial_files(self):
        for failed in ("stats", "snake"):
            with self.subTest(failed=failed):
                write_pair(self.previous, "stats", "old stats")
                write_pair(self.previous, "snake", "old snake")
                write_pair(self.stats, "stats", "new stats")
                write_pair(self.snake, "snake", "new snake")
                result = self.assemble(stats_ok=failed != "stats", snake_ok=failed != "snake")
                self.assertEqual(result, {"can_publish": True, "degraded": True})
                for name in assets.PAIRS[failed]:
                    self.assertIn("old " + failed, (self.output / name).read_text())

    def test_invalid_or_missing_half_preserves_the_whole_old_pair(self):
        write_pair(self.previous, "stats", "old stats")
        write_pair(self.stats, "stats", "new stats")
        write_pair(self.snake, "snake", "new snake")
        (self.stats / "stats-dark.svg").write_text("<svg>broken")
        self.assertEqual(self.assemble(), {"can_publish": True, "degraded": True})
        for name in assets.PAIRS["stats"]:
            self.assertIn("old stats", (self.output / name).read_text())

    def test_no_valid_fallback_prevents_deleting_a_published_pair(self):
        write_pair(self.stats, "stats", "new stats")
        self.assertEqual(self.assemble(snake_ok=False), {"can_publish": False, "degraded": True})
        self.assertFalse(self.output.exists())

    def test_both_generators_failed_leaves_output_untouched(self):
        write_pair(self.previous, "stats", "old stats")
        write_pair(self.previous, "snake", "old snake")
        self.assertEqual(self.assemble(False, False), {"can_publish": False, "degraded": True})
        self.assertFalse(self.output.exists())

    def test_failed_git_show_does_not_create_empty_snapshot_file(self):
        results = [subprocess.CompletedProcess([], 0)] + [
            subprocess.CompletedProcess([], 1, stdout=b"", stderr=b"missing") for _ in range(4)
        ]
        with mock.patch.object(assets.subprocess, "run", side_effect=results) as git:
            assets.snapshot(self.previous)
        self.assertIn("+refs/heads/output:refs/remotes/origin/output", git.call_args_list[0].args[0])
        self.assertEqual(list(self.previous.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
