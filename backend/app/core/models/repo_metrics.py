from dataclasses import dataclass

@dataclass
class RepoActivityMetrics:
    commits_last_30_days: int
    issues_closed_last_30_days: int
    prs_merged_last_30_days: int

@dataclass
class RepoResponsiveMetrics:
    avg_issue_response_hours: float
    avg_pr_review_hours: float
    issue_close_rate: float
    pr_merge_rate: float

