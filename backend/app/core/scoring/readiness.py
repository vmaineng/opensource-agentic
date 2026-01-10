from enum import Enum
from typing import List

class Persona(Enum):
    JUNIOR_DEVELOPER = "junior_developer"
    EXPERIENCED_CONTRIBUTOR = "experienced_contributor"
    EXPLORER = "explorer"

READINESS_PERSONA_PRESETS = {
    Persona.JUNIOR_DEVELOPER.value: {"activity": 0.4, "responsiveness": 0.6},
    Persona.EXPERIENCED_CONTRIBUTOR.value: {"activity": 0.6, "responsiveness": 0.4},
    Persona.EXPLORER.value: {"activity": 0.5, "responsiveness": 0.5},
}


def calculate_contribution_readiness_score(activity_score: int, responsiveness_score: int, persona: Persona = Persona.JUNIOR_DEVELOPER, community_score: int = 0) -> int:
    weights = READINESS_PERSONA_PRESETS.get(persona.value)

    if not weights:
        raise ValueError(f"Unknown persona: {persona}")
    
    community_weight = 0.1
    base_weight_total = sum(weights.values())
    total_weight = base_weight_total + community_weight

    weighted_score = (
        activity_score * weights["activity"] +
        responsiveness_score * weights["responsiveness"] + 
        community_score * community_weight
    ) / total_weight
    return round(weighted_score)

def explain_contribution_readiness(
    activity_score: int,
    responsiveness_score: int,
    persona: Persona = Persona.JUNIOR_DEVELOPER,
    community_score: int = 0
) -> List[str]:
    reasons = []

    if activity_score < 40:
        reasons.append("Low recent activity.")
    elif activity_score >= 70:
        reasons.append("Active development.")

    if responsiveness_score < 40 and persona == Persona.JUNIOR_DEVELOPER:
        reasons.append("Maintainers may be slow to respond to new contributors.")
    elif responsiveness_score >= 70:
        reasons.append("Responsive maintainers.")

    if community_score > 0:
        if community_score >= 50:
         reasons.append(f"Community engagement is {community_score}.")
        else:
            reasons.append(f"Some community engagement with a score of {community_score}.")

    return reasons
