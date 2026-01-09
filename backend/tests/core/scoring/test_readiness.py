from app.core.scoring.readiness import calculate_contribution_readiness_score, explain_contribution_readiness, Persona

def test_junior_persona_score():
    score = calculate_contribution_readiness_score(
        activity_score=80,
        responsiveness_score=40,
        persona=Persona.JUNIOR_DEVELOPER,

    )
    assert score == 56
    