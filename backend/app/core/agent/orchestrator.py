from app.core.agent.selector import auto_select_persona
from app.core.scoring.readiness import calculate_contribution_readiness_score, explain_contribution_readiness
from app.core.agent.models import ContributionReadinessResult
from app.core.scoring.community import calculate_community_score
from app.core.scoring.community import RepoCommunityMetrics

def assess_contribution_readiness(
        contributor_metrics: dict,
        activity_score: int, 
        responsiveness_score: int,
        community_metrics: RepoCommunityMetrics | dict = None
) -> ContributionReadinessResult:
    persona_result = auto_select_persona(contributor_metrics)

    if community_metrics:
        community_score = calculate_community_score(community_metrics)
    else:
        community_score = 0
    
    readiness_score = calculate_contribution_readiness_score(
        activity_score=activity_score,
        responsiveness_score=responsiveness_score,
        community_score=community_score,
        persona=persona_result.persona
    )

    readiness_reasons = explain_contribution_readiness(
        activity_score=activity_score,
        responsiveness_score=responsiveness_score,
        persona=persona_result.persona  
    )

    combined_reasons = persona_result.reasons + readiness_reasons
    if community_score > 0:
        combined_reasons.append(f"Community engagement contributed a score of {community_score}.")
    
    return ContributionReadinessResult(
        persona=persona_result.persona,
        readiness_score=readiness_score,
        reasons=combined_reasons
    )


