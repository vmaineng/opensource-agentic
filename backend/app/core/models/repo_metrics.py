from dataclasses import dataclass

@dataclass
class RepoActivityMetrics:
    commits_last_30_days: int
    issues_closed_last_30_days: int
    prs_merged_last_30_days: int