
from jargonprofiler.munroe import munroe_score


def test_all_common():
    assert munroe_score("The address of the administration is 1000 green road.",
                        verbose=True) == 100


def test_all_jargon():
    assert munroe_score("epigenetics magic navy") == 0
