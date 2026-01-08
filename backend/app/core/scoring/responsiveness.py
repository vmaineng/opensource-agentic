from app.core.models.repo_metrics import RepoResponsiveMetrics
from app.core.scoring.normalization import normalize_score

MAX_RESPONSIVENESS_RAW_SCORE = 100.0

def calculate_responsiveness_raw(metrics: RepoResponsiveMetrics) -> float:
    score = 0.0
    score += max(0, 72- metrics.avg_issue_response_hours) * 0.4
    score += max(0, 72 - metrics.avg_pr_review_hours) * 0.3
    score += metrics.issue_close_rate * 20
    score += metrics.pr_merge_rate * 20
    return score

def calculate_responsiveness_score(metrics: RepoResponsiveMetrics) -> int:
    raw = calculate_responsiveness_raw(metrics)
    normalized_score = normalize_score(raw, MAX_RESPONSIVENESS_RAW_SCORE)
    return normalized_score