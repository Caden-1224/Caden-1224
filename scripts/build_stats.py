#!/usr/bin/env python3
"""Build the GitHub profile statistics cards.

The cards intentionally expose only metrics with an unambiguous public meaning:

* ``stars`` is the sum of stargazers on the account's public, owned,
  non-fork repositories.
* ``repos`` is the number of those repositories.

A commit total is deliberately not shown.  GitHub's repository commit API
counts every contributor, so presenting that number as the account owner's
commits would be misleading.  The script uses the public API when no token is
provided; ``GITHUB_TOKEN``/``GH_TOKEN`` simply raises the rate limit.

    python scripts/build_stats.py dist
    GITHUB_TOKEN=... STATS_DATE=2026-01-01 python scripts/build_stats.py dist
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
LOGIN = os.environ.get("STATS_USER", "Caden-1224")

CARD_W, CARD_H = 460, 176
MAX_ATTEMPTS = 4
RETRYABLE_STATUS = {408, 425, 429, 500, 502, 503, 504}

LIGHT = {
    "card": "#ffffff", "border": "#d3e2f1", "dot": "#e2ecf8", "hair": "#e2ecf8",
    "title": "#526b86", "number": "#12304e", "note": "#526b86",
    "red": "#e0483c", "blue": "#2f6fd0",
}
DARK = {
    "card": "#0d1a2c", "border": "#22405f", "dot": "#1a2c46", "hair": "#1e3050",
    "title": "#a2b8d3", "number": "#eef4fb", "note": "#a2b8d3",
    "red": "#ff6b5e", "blue": "#5a9be6",
}

STAR = ("M0 -10L2.351 -3.236L9.511 -3.09L3.804 1.236L5.878 8.09L0 4"
        "L-5.878 8.09L-3.804 1.236L-9.511 -3.09L-2.351 -3.236Z")


def _retry_delay(exc: urllib.error.HTTPError, attempt: int) -> float | None:
    """Respect short Retry-After delays; leave long limits to the next run."""
    retry_after = exc.headers.get("Retry-After", "") if exc.headers else ""
    try:
        delay = max(0.0, float(retry_after))
        return delay if delay <= 30 else None
    except (TypeError, ValueError):
        return 2 ** attempt


def rest(path: str) -> tuple[Any, Any]:
    """GET a GitHub API path, retrying transient failures."""
    req = urllib.request.Request(API + path)
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "caden-profile-assets")
    for attempt in range(MAX_ATTEMPTS):
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                body = response.read().decode("utf-8")
                return response, json.loads(body)
        except urllib.error.HTTPError as exc:
            # GitHub also uses 403 for secondary rate limits. A primary limit
            # can last an hour; fail visibly instead of publishing fake zeros.
            secondary_limit = (exc.code == 403 and exc.headers
                               and exc.headers.get("Retry-After") is not None)
            if (exc.code not in RETRYABLE_STATUS and not secondary_limit) or attempt == MAX_ATTEMPTS - 1:
                raise
            delay = _retry_delay(exc, attempt)
            if delay is None:
                raise
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError):
            if attempt == MAX_ATTEMPTS - 1:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


def _repo_page(page: int) -> str:
    query = urllib.parse.urlencode({"per_page": 100, "type": "owner", "sort": "full_name",
                                    "direction": "asc", "page": page})
    return "/users/%s/repos?%s" % (urllib.parse.quote(LOGIN, safe=""), query)


def _validate_repo(repo: Any) -> None:
    """Reject incomplete API data rather than silently publishing false totals."""
    if not isinstance(repo, dict):
        raise ValueError("GitHub repository response was not an object")
    for field in ("id", "stargazers_count"):
        if type(repo.get(field)) is not int or repo[field] < 0:
            raise ValueError("GitHub repository has invalid " + field)
    for field in ("fork", "private"):
        if type(repo.get(field)) is not bool:
            raise ValueError("GitHub repository has invalid " + field)
    owner = repo.get("owner")
    if not isinstance(owner, dict) or not isinstance(owner.get("login"), str) or not owner["login"]:
        raise ValueError("GitHub repository has invalid owner.login")


def collect() -> dict[str, Any]:
    """Collect public owned repository facts for ``LOGIN``."""
    repos: dict[int, dict[str, Any]] = {}
    page = 1
    while True:
        _, chunk = rest(_repo_page(page))
        if not isinstance(chunk, list):
            raise ValueError("GitHub repositories response was not a list")
        previous_count = len(repos)
        for repo in chunk:
            _validate_repo(repo)
            # A repository can move between pages while the request runs.
            # Its stable ID prevents that from inflating the totals.
            repos[repo["id"]] = repo
        if len(chunk) < 100:
            break
        if len(repos) == previous_count:
            raise ValueError("GitHub pagination returned a repeated full page")
        page += 1

    owned_public = [
        repo for repo in repos.values()
        if not repo["fork"] and not repo["private"]
        and repo["owner"]["login"].casefold() == LOGIN.casefold()
    ]
    return {
        "login": LOGIN,
        "stars": sum(repo["stargazers_count"] for repo in owned_public),
        "repos": len(owned_public),
    }


def fmt(value: int) -> str:
    return f"{value:,}"


def card(stats: dict[str, Any], palette: dict[str, str], updated: str) -> str:
    login = html.escape(str(stats["login"]), quote=True)
    login_upper = html.escape(str(stats["login"]).upper(), quote=True)
    updated_short = datetime.fromisoformat(updated.replace("Z", "+00:00")).strftime("%m-%d %H:%M")
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{login} on GitHub: {stars} stars across {repos} owned public non-fork repositories; updated {updated}">
  <title>{login} - {stars} stars, {repos} owned public non-fork repositories</title>
  <desc>Public repositories owned by {login}, excluding forks. Includes archived repositories. Last successful update: {updated}.</desc>
  <defs>
    <pattern id="dotgrid" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="{dot}"/></pattern>
  </defs>
  <rect x="1" y="1" width="{iw}" height="{ih}" rx="10" fill="{card}" stroke="{border}" stroke-width="2"/>
  <rect x="1" y="1" width="{iw}" height="{ih}" rx="10" fill="url(#dotgrid)"/>
  <path d="M26 34H46" stroke="{red}" stroke-width="2"/>
  <text x="54" y="39" font-family="Consolas, monospace" font-size="11" letter-spacing="1.6" fill="{title}">{login_upper} / GITHUB STATS</text>
  <path d="M230 62V138" stroke="{hair}" stroke-width="1.5"/>
  <g transform="translate(40 86)"><path d="{star}" fill="{red}"/></g>
  <text x="62" y="98" font-family="Segoe UI, Arial, sans-serif" font-size="34" font-weight="650" fill="{number}">{stars}</text>
  <text x="28" y="130" font-family="Consolas, monospace" font-size="10" letter-spacing="1.4" fill="{title}">PUBLIC STARS</text>
  <g transform="translate(270 86)">
    <rect x="-8" y="-9" width="16" height="18" rx="3" fill="none" stroke="{blue}" stroke-width="2"/>
    <path d="M-4 -3H4M-4 2H4" stroke="{blue}" stroke-width="2" stroke-linecap="round"/>
  </g>
  <text x="292" y="98" font-family="Segoe UI, Arial, sans-serif" font-size="34" font-weight="650" fill="{number}">{repos}</text>
  <text x="258" y="130" font-family="Consolas, monospace" font-size="10" letter-spacing="1.4" fill="{title}">PUBLIC REPOS</text>
  <path d="M26 148H434" stroke="{hair}" stroke-width="1.5"/>
  <text x="26" y="166" font-family="Consolas, monospace" font-size="9" letter-spacing="0.5" fill="{note}">UPDATED {updated_short} UTC</text>
  <text x="434" y="166" text-anchor="end" font-family="Consolas, monospace" font-size="9" letter-spacing="0.5" fill="{note}">OWNED · NON-FORK</text>
</svg>
""".format(w=CARD_W, h=CARD_H, iw=CARD_W - 2, ih=CARD_H - 2,
           login=login, login_upper=login_upper, stars=fmt(stats["stars"]),
           repos=stats["repos"],
           updated=html.escape(updated), updated_short=updated_short, star=STAR, **palette)


def _updated_date() -> str:
    candidate = (os.environ.get("STATS_DATE") or "").strip()
    if candidate:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", candidate):
            raise ValueError("STATS_DATE must use YYYY-MM-DD")
        datetime.strptime(candidate, "%Y-%m-%d")
        return candidate + "T00:00Z"
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def _write_atomic(path: str, content: str) -> None:
    directory = os.path.dirname(path) or "."
    fd, temp_path = tempfile.mkstemp(prefix=".stats-", suffix=".svg", dir=directory, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        os.replace(temp_path, path)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def main() -> None:
    updated = _updated_date()
    outdir = sys.argv[1] if len(sys.argv) > 1 else "dist"
    os.makedirs(outdir, exist_ok=True)
    stats = collect()
    print("stars   : %d" % stats["stars"])
    print("repos   : %d" % stats["repos"])
    for name, palette in (("stats", LIGHT), ("stats-dark", DARK)):
        path = os.path.join(outdir, name + ".svg")
        _write_atomic(path, card(stats, palette, updated))
        print("wrote %s" % path)


if __name__ == "__main__":
    main()
