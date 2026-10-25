#!/usr/bin/env python3
"""Select complete, valid SVG pairs before publishing profile assets.

Generators write into separate directories. A failed or incomplete generation
can never replace one half of a previously published light/dark pair.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

PAIRS = {
    "stats": ("stats.svg", "stats-dark.svg"),
    "snake": ("github-contribution-grid-snake.svg", "github-contribution-grid-snake-dark.svg"),
}


def snapshot(directory: Path) -> None:
    """Read the exact output ref without creating empty fallback files."""
    result = subprocess.run(
        ["git", "fetch", "--no-tags", "--depth=1", "origin",
         "+refs/heads/output:refs/remotes/origin/output"],
        check=False,
    )
    if result.returncode:
        print("Previous output could not be fetched; only complete new assets can be published.")
        return
    directory.mkdir(parents=True, exist_ok=True)
    for names in PAIRS.values():
        for name in names:
            result = subprocess.run(
                ["git", "show", "refs/remotes/origin/output:" + name],
                capture_output=True, check=False,
            )
            if result.returncode == 0 and result.stdout:
                (directory / name).write_bytes(result.stdout)


def read_pair(directory: Path, names: tuple[str, str]) -> dict[str, bytes] | None:
    assets = {}
    for name in names:
        try:
            content = (directory / name).read_bytes()
            root = ET.fromstring(content)
            if root.tag != "{http://www.w3.org/2000/svg}svg" or not len(root):
                raise ValueError("not a populated SVG document")
        except (OSError, ET.ParseError, ValueError) as exc:
            print(f"Rejected {directory / name}: {exc}")
            return None
        assets[name] = content
    return assets


def assemble(previous: Path, stats: Path, snake: Path, output: Path,
             stats_ok: bool, snake_ok: bool) -> dict[str, bool]:
    selected: dict[str, bytes] = {}
    fresh = 0
    degraded = False
    complete = True
    for kind, directory, succeeded in (("stats", stats, stats_ok), ("snake", snake, snake_ok)):
        names = PAIRS[kind]
        assets = read_pair(directory, names) if succeeded else None
        if assets is not None:
            fresh += 1
            print(f"{kind}: using newly generated pair")
        else:
            degraded = True
            assets = read_pair(previous, names)
            if assets is not None:
                print(f"{kind}: retaining previously published pair")
        if assets is None:
            complete = False
            print(f"{kind}: no complete valid pair is available")
        else:
            selected.update(assets)

    can_publish = complete and fresh > 0
    if can_publish:
        output.mkdir(parents=True, exist_ok=True)
        for name, content in selected.items():
            (output / name).write_bytes(content)
    return {"can_publish": can_publish, "degraded": degraded}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    previous = sub.add_parser("snapshot")
    previous.add_argument("directory", type=Path)
    publish = sub.add_parser("assemble")
    publish.add_argument("--previous", type=Path, default=Path("previous"))
    publish.add_argument("--stats", type=Path, default=Path("stats-next"))
    publish.add_argument("--snake", type=Path, default=Path("snake-next"))
    publish.add_argument("--output", type=Path, default=Path("dist"))
    publish.add_argument("--stats-outcome", choices=("success", "failure", "skipped", "cancelled"), required=True)
    publish.add_argument("--snake-outcome", choices=("success", "failure", "skipped", "cancelled"), required=True)
    args = parser.parse_args()
    if args.command == "snapshot":
        snapshot(args.directory)
        return
    result = assemble(args.previous, args.stats, args.snake, args.output,
                      args.stats_outcome == "success", args.snake_outcome == "success")
    lines = "".join(f"{key}={str(value).lower()}\n" for key, value in result.items())
    print(lines, end="")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
            handle.write(lines)


if __name__ == "__main__":
    main()
