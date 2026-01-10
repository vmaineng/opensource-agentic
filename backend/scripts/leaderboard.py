from app.core.agent.orchestrator import assess_contribution_readiness
from app.core.scoring.models import RepoCommunityMetrics
from app.core.agent.models import PersonaSelectionResult

contributors = [
    {
        "name": "Alice",
        "metrics": {
            "prior_contributions": 5,
            "years_experience": 3
        },
        "community_metrics": RepoCommunityMetrics(
            issues_commented_last_30_days=15,
            prs_commented_last_30_days=4,
            forum_posts_last_30_days=8 
        ),
        "activity_score": 85,
        "responsiveness_score": 70
    },
     {
        "name": "Bob",
        "metrics": {
            "prior_contributions": 2,
            "years_experience": 1
        },
        "community_metrics": RepoCommunityMetrics(
            issues_commented_last_30_days=1,
            prs_commented_last_30_days=0,
            forum_posts_last_30_days=1 
        ),
        "activity_score": 60,
        "responsiveness_score": 40
    },
]

leaderboard = []

for contributor in contributors:
    result = assess_contribution_readiness(
        contributor_metrics=contributor["metrics"],
        activity_score=contributor["activity_score"],
        responsiveness_score=contributor["responsiveness_score"],
        community_metrics=contributor["community_metrics"]
    )
    leaderboard.append({
        "name": contributor["name"],
        "readiness_score": result.readiness_score,
        "persona": result.persona,
        "reasons": result.reasons
    })

leaderboard.sort(key=lambda x: x["readiness_score"], reverse=True)

print("\n===Contributor Leaderboard ===")
for rank, entry in enumerate(leaderboard, start=1):
    print(f"{i}. {entry['name']} ({entry['persona']}) - Score: {entry['readiness_score']}")
    for reason in entry['reasons']:
        print(f"   - {reason}")
    print()

average_score = sum(entry['readiness_score'] for entry in leaderboard) / len(leaderboard)
print(f"Average Contribution Readiness Score: {average_score:.2f}")