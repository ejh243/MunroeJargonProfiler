
from jargonprofiler.util import tag_proper_nouns
from jargonprofiler.munroe import munroe_score


def test_proper_noun_in_sentance():
    assert tag_proper_nouns("My name is Eilis.") == set(["Eilis"])


def test_proper_noun_begins_sentance():
    assert tag_proper_nouns("Eilis is a girl") == set(["Eilis"])


def test_munroe_with_proper_nouns():
    result = munroe_score("Eilis is a small girl")
    assert result["score"] == 1.0
