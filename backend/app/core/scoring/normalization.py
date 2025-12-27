def normalize_score(raw_score: float, max_raw_score: float) -> int:
    if raw_score <= 0:
        return 0
    if raw_score >= max_raw_score:
        return 100
    normalized = (raw_score / max_raw_score) * 100
    return round(normalized)