
from jargonprofiler.munroe import munroe_score


def test_uk_english():
    assert munroe_score("realise centre") == 100
