from app.core.scoring.normalization import normalize_score

def test_normalize_score():
    assert normalize_score(0,100) == 0

def test_normalize_score_caps_at_100():
    assert normalize_score(150,100) == 100

def test_normalize_score_mid_value():
    assert normalize_score(50,100) == 50