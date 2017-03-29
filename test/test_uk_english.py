
from jargonprofiler.munroe import munroe_score


def test_uk_english():
    '''The current word list has US spellings.'''
    result = munroe_score("realise centre")
    assert result["score"] == 0.0
