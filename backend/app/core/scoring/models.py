from dataclasses import dataclass

@dataclass
class RepoCommunityMetrics:
    issues_commented_last_30_days: int
    prs_commented_last_30_days: int
    forum_posts_last_30_days: int