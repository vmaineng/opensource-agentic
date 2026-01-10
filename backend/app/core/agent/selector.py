from app.core.scoring.reading import Persona
from app.core.agent.models import PersonaSelectionResult

def auto_select_persona(metrics: dict) -> PersonaSelectionResult:
    contributions = contributor_metrics.get("prior_contributions", 0)
    experience = contributor_metrics.get("years_experience", 0)

    reasons = list[str] = []

    if contributions < 5 and experience < 2:
        reasons.append("Few prior contributions and limited experience.")
        reasons.append("Limited professional experience.")
        return PersonaSelectionResult(
            persona=Persona.JUNIOR_DEVELOPER,
            reasons=reasons
        )
    
    if contributions >= 20 and experience >= 5:
        reasons.append("Significant prior contributions.")
        reasons.append("Extensive professional experience.")
        return PersonaSelectionResult(
            persona=Persona.EXPERIENCED_CONTRIBUTOR,
            reasons=reasons
        )
    reasons.append("Moderate contributions and experience.")
    return PersonaSelectionResult(
        persona=Persona.EXPLORER,
        reasons=reasons
    )