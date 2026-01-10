from app.core.scoring.normalization import normalize_score
from app.core.scoring.models import RepoCommunityMetrics

MAX_COMMUNITY_RAW_SCORE = 100.0

def calculate_raw_community_score(metrics:RepoCommunityMetrics) -> float:
    score = (
        metrics.issues_commented_last_30_days * 1.0 + 
        metrics.prs_commented_last_30_days * 1.5 + 
        metrics.forum_posts_last_30_days * 2.0
    )
    return score

def calculate_community_score(metrics:RepoCommunityMetrics) -> int:
    raw_score = calculate_raw_community_score(metrics)
    normalized_score = normalize_score(raw_score, MAX_COMMUNITY_RAW_SCORE)
    return normalized_score