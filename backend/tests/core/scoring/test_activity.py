from app.core.models.repo_metrics import RepoActivityMetrics
from app.core.scoring.activity import calculate_raw_activity_score

def test_calculate_raw_activity_score():
    metrics = RepoActivityMetrics(
        commits_last_30_days=10,
        issues_closed_last_30_days=5,
        prs_merged_last_30_days=2
    )
    score = calculate_raw_activity_score(metrics)
    expected_score = (10 * 2) + (5 * 1.5) + (2 * 3.0)  # 20 + 7.5 + 6 = 33.5
    assert score == expected_score