from app.core.models.repo_metrics import RepoActivityMetrics

def calculate_raw_activity_score(metrics: RepoActivityMetrics) -> int:
    score = (
        metrics.commits_last_30_days * 2 +
        metrics.issues_closed_last_30_days * 1.5 +
        metrics.prs_merged_last_30_days * 3.0
    )
    return score