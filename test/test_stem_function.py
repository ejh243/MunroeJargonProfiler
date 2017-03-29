
from jargonprofiler.munroe import munroe_score


def test_stem_words_for_score():
    assert munroe_score("joining laughing supported computers riches") == 100
