from app.core.scoring.agent import auto_select_persona
from app.core.scoring.readiness import Persona


def test_auto_select_persona_junior():
    metrics = {
        "prior_contributions": 2,
        "years_experience": 1,
        "goal": "learning",
    }
    persona = auto_select_persona(metrics)
    assert persona == Persona.JUNIOR_DEVELOPER