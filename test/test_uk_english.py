
from jargonprofiler.munroe import munroe_score


def test_uk_english():
    result = munroe_score("realise centre")
    assert result["score"] == 100
