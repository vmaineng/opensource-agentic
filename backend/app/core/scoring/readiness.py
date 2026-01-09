from typing import List

ACTIVITY_WEIGHT = 0.5
RESPONSIVENESS_WEIGHT = 0.5

def calculate_contribution_readiness_score(activity_score: int, responsiveness_score: int) -> int:
    weighted_activity = (
        activity_score * ACTIVITY_WEIGHT + responsiveness_score * RESPONSIVENESS_WEIGHT
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