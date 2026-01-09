from typing import List

DEFAULT_READINESS_WEIGHTS = {
    "activity": 0.5,
    "responsiveness": 0.5,
}

def calculate_contribution_readiness_score(activity_score: int, responsiveness_score: int, weights: dict = DEFAULT_READINESS_WEIGHTS) -> int:
    weighted_activity = (
        activity_score * weights['activity'] + responsiveness_score * weights['responsiveness']
    )
    return round(weighted_activity)

def explain_contribution_readiness(activity_score: int, responsiveness_score: int) -> List[str]:
    reasons = []
    if activity_score < 40:
        reasons.append("Low recent activity.")
    elif activity_score >= 70:
        reasons.append("Active development.")
    if responsiveness_score < 40:
        reasons.append("Slow maintainer responses.")
    elif responsiveness_score >= 70:
        reasons.append("Responsive maintainers.")
    return reasons