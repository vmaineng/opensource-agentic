import pytest
from unittest.mock import patch

from app.core.agent.orchestrator import assess_contribution_readiness
from app.core.agent.models import ContributionReadinessResult , PersonaSelectionResult
from app.core.scoring.readiness import Persona  
from app.core.scoring.models import RepoCommunityMetrics
from app.core.scoring.community import calculate_community_score

def test_assess_contribution_readiness_combines_reason():

    contributor_metrics = {
        "prior_contributions": 1,
        "years_experience": 1
    }
    activity_score = 80
    responsiveness_score = 40
    community_metrics = RepoCommunityMetrics(
        issues_commented_last_30_days=10,
        prs_commented_last_30_days=2,
        forum_posts_last_30_days=5
    )

    with patch('app.core.agent.orchestrator.auto_select_persona') as mock_selector:
        mock_selector.return_value = PersonaSelectionResult(
            persona=Persona.JUNIOR_DEVELOPER,
            reasons=["Mocked persona reason."]
        )

        result = assess_contribution_readiness(
            contributor_metrics={"prior_contributions": 1, "years_experience": 1},
            activity_score=80,
            responsiveness_score=40,
            community_metrics=community_metrics
        )   
   
    assert "Mocked persona reason." in result.reasons
    assert any("Active development" in r for r in result.reasons )
    expected_msg = f"Community engagement contributed a score of {calculate_community_score(community_metrics)}."
    assert expected_msg in result.reasons
