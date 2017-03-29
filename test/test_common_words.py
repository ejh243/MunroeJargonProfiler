
from jargonprofiler.munroe import munroe_score


def test_all_common():
    result = munroe_score("The address of the administration is 1000 green road.",
                          verbose=True)
    assert result["score"] == 1.0


def test_half_jargon():
    assert munroe_score("epigenetics address")['score'] == 0.5


def test_all_jargon():
    result = munroe_score("epigenetics magic navy")
    assert result["score"] == 0.0
