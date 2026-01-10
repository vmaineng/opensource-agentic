from app.core.agent.selector import auto_select_persona
from app.core.scoring.readiness import calculate_contribution_readiness_score, explain_contribution_readiness
from app.core.agent.models import ContributionReadinessResult

def assess_contribution_readiness(
        contributor_metrics: dict,
        activity_score: int, 
        responsive_score: int,
) -> ContributionReadinessResult:
    persona_result = auto_select_persona(contributor_metrics)
    
    readiness_score = calculate_contribution_readiness_score(
        activity_score=activity_score,
        responsiveness_score=responsive_score,
        persona=persona_result.persona
    )

    readiness_reasons = explain_contribution_readiness(
        activity_score=activity_score,
        responsiveness_score=responsive_score,
        persona=persona_result.persona  
    )

    combined_reasons = persona_result.reasons + readiness_reasons
    return ContributionReadinessResult(
        persona=persona_result.persona,
        readiness_score=readiness_score,
        reasons=combined_reasons
    )