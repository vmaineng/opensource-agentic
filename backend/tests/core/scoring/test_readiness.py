from app.core.scoring.readiness import calculate_contribution_readiness_score, explain_contribution_readiness

def test_contribution_readiness_score_calculation():
    activity_score = 80
    responsiveness_score = 70
    readiness_score = calculate_contribution_readiness_score(activity_score, responsiveness_score)
    assert readiness_score == 75  

def test_low_contribution_readiness_score():
    activity_score = 30
    responsiveness_score = 20
    readiness_score = calculate_contribution_readiness_score(activity_score, responsiveness_score)
    assert readiness_score == 25

def test_explanation_for_high_scores():
    activity_score = 85
    responsiveness_score = 90
    reasons = explain_contribution_readiness(activity_score, responsiveness_score)
    assert "Active development." in reasons
    assert "Responsive maintainers." in reasons

def test_explanation_for_low_scores():
    activity_score = 25
    responsiveness_score = 30
    reasons = explain_contribution_readiness(activity_score, responsiveness_score)
    assert "Low recent activity." in reasons
    assert "Slow maintainer responses." in reasons