# Profile asset maintenance

`profile-assets.yml` is scheduled every ten minutes (`*/10 * * * *`, UTC).
GitHub runs scheduled workflows on a best-effort basis: high-frequency intervals
are queued behind other runs and may be delayed or dropped during periods of high
load, so ten minutes is a target rather than a guarantee. Each run rebuilds both
the card and the snake, and each run pushes to `output`, so the repository never
goes inactive and the schedule stays enabled. The workflow also runs
on pushes to `main` and supports a manual run from the Actions tab. A successful run
publishes `stats.svg`, `stats-dark.svg`, and the contribution snake to the
`output` branch; GitHub's raw URLs in the profile README then pick up the new
files after normal CDN cache expiry. The card footer displays the time of the
last successful refresh in UTC, including hours and minutes; its SVG description
contains the full ISO timestamp. A page refresh does not force a new API fetch.

The statistics card intentionally reports only:

- **Public stars**: the sum of `stargazers_count` for public repositories owned
  by `Caden-1224`, excluding forks.
- **Public repos**: the number of those repositories.

It does not report a commit total. The repository commits endpoint counts every
author, so that number cannot truthfully be presented as Caden's commits.
Archived repositories remain included because they are still public owned
projects. Private repositories are excluded from the count.

To preview the card locally, run `python scripts/build_stats.py dist`. The
public GitHub API works without a token; setting `GITHUB_TOKEN` (or `GH_TOKEN`)
raises the API rate limit for a scheduled run. For reproducible previews,
`STATS_DATE=YYYY-MM-DD` pins the timestamp to that date at 00:00 UTC. Scheduled
runs leave that override unset and show the actual refresh time. API failures or
malformed responses fail visibly instead of being counted as zero. Short
transient failures are retried; a long rate-limit delay is left for the next run.

The stats and snake generators write to isolated directories. Before publication,
`scripts/assemble_assets.py` checks that both SVGs in each light/dark pair are
present and valid. If one generator fails or produces an incomplete pair, the
previous complete pair is retained and the other generator's valid update can
still publish. Partial files never overwrite the previous pair. If both fail,
or a missing fallback would leave the profile with broken links, the `output`
branch is left untouched. A degraded run is marked as failed in Actions even
when the other asset pair published successfully.

The workflow fetches the explicit `output` ref before taking its snapshot and
serializes publication to avoid overlapping scheduled/manual runs. If that
branch is unavailable, publication requires complete new pairs from both
generators. The first successful run creates the branch.

Run the offline checks with `python -m unittest discover -s tests -v`. They
exercise pagination, metric scope, API failures, malformed data, timestamp
formatting, and complete-pair fallback before a workflow can publish assets.

## Keeping profile information consistent

`README.md` and `README.en.md` are the Chinese and English versions of the
same profile. Update the matching sections together when a project reaches a
new milestone. Project descriptions are curated text, not generated from the
repository About field; counts and the contribution calendar are the automated
parts. Use each project's current README and validation records as the source
for implemented capabilities, and distinguish future plans from delivered work.

The September 24, 2026 review found a separate discrepancy in the NexWeave
repository's About description: it implies RK3576 voice interaction is already
implemented, while its README explicitly says real models and board integration
are not complete. That external setting is not changed by editing this profile.
A description consistent with its current README would be:

> 面向 Linux 边缘设备的 C++17 任务框架，围绕会话生命周期、有界数据流、跨进程取消与旧结果隔离建立统一契约；当前验证 Linux 多进程核心，真实模型与 RK3576 接入尚未完成。

Publishing these local changes to `main` is what activates the revised schedule
and image generation workflow. Until then, the live profile still uses the old
README and the previously published assets. For visual changes, check both
languages, light/dark themes and a narrow viewport. The SVGs and PNG banner are
local assets; the stats and snake URLs intentionally refer to the `output`
branch. GitHub rendering and CDN caches may take time to reflect an update.
