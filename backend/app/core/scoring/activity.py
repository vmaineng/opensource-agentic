from app.core.models.repo_metrics import RepoActivityMetrics
from app.core.scoring.normalization import normalize_score

MAX_ACTIVITY_RAW_SCORE = 100.0 

def calculate_raw_activity_score(metrics: RepoActivityMetrics) -> float:
    score = (
        metrics.commits_last_30_days * 2.0 +
        metrics.issues_closed_last_30_days * 1.5 +
        metrics.prs_merged_last_30_days * 3.0
    )
    return score

def calucate_activity_score(metrics: RepoActivityMetrics) -> int:
    raw_score = calculate_raw_activity_score(metrics)
    normalized_score = normalize_score(raw_score, MAX_ACTIVITY_RAW_SCORE)
    return normalized_score