
from jargonprofiler.util import tag_proper_nouns
from jargonprofiler.munroe import munroe_score


def test_proper_noun_in_sentence():
    assert tag_proper_nouns("My name is Eilis.") == set(["Eilis"])


def test_proper_noun_begins_sentence():
    assert tag_proper_nouns("Eilis is a girl") == set(["Eilis"])


def test_proper_noun_middle_sentence():
    assert tag_proper_nouns("Today, Eilis is at CW17.") == set(["Eilis"])


def test_proper_noun_missing():
    assert tag_proper_nouns("Today is cloudy at CW17.") == set()


def test_two_proper_nouns():
    assert tag_proper_nouns("Eilis Hannon is a girl.") == set(["Eilis",
                                                               "Hannon"])


def test_munroe_with_proper_noun():
    result = munroe_score("Eilis is a small girl")
    assert result["score"] == 1.0
    assert result['tagged_words'] == {
        'Eilis': 'proper noun', 'a': 'not alphabetic',
        'is': 'not alphabetic', 'small': 'common', 'girl': 'common'
    }


def test_munroe_with_proper_noun_and_complex_words():
    result = munroe_score("Jonathan and Eilis are at a workshop")
    assert result['score'] == 1 / 3
    assert result['tagged_words'] == {
        'Jonathan': 'proper noun', 'Eilis': 'proper noun',
        'at': 'not alphabetic', 'a': 'not alphabetic', 'and': 'common',
        'workshop': 'not common', 'are': 'not common'
    }
