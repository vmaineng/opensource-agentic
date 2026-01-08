from app.core.scoring.responsiveness import calculate_responsiveness_score, RepoResponsiveMetrics

def test_high_responsiveness_scores_high():
    metrics = RepoResponsiveMetrics(
        avg_issue_response_hours=6,
        avg_pr_review_hours=8,
        issue_close_rate=0.9,
        pr_merge_rate=0.85
    )
    score = calculate_responsiveness_score(metrics)
    assert score >= 80

def test_low_responsiveness_scores_low():
    metrics = RepoResponsiveMetrics(
        avg_issue_response_hours=200,
        avg_pr_review_hours=300,
        issue_close_rate=0.1,
        pr_merge_rate=0.05
    )
    score = calculate_responsiveness_score(metrics)
    assert score <= 30

def test_responsiveness_score_non_negative():
    metrics = RepoResponsiveMetrics(
        avg_issue_response_hours=999,
        avg_pr_review_hours=999,
        issue_close_rate=0.0,
        pr_merge_rate=0.0
    )
    score = calculate_responsiveness_score(metrics)
    assert score == 0