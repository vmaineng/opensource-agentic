from app.core.scoring.readiness import Persona

def auto_select_persona(contributor_metrics: dict) -> Persona:
    contributions = contributor_metrics.get("prior_contributions", 0)
    experience = contributor_metrics.get("years_experience", 0)
    goal = contributor_metrics.get("goal", "learning")

    if contributions <5 and experience < 2:
        return Persona.JUNIOR_DEVELOPER
    elif contributions >= 20 or experience >= 5:
        return Persona.EXPERIENCED_CONTRIBUTOR
    else:
        return Persona.EXPLORER