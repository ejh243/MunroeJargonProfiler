
from jargonprofiler.munroe import munroe_score


def test_stem_words_for_score():
    result = munroe_score("joining laughing supported computers riches")
    assert result["basic_score"] == 100
