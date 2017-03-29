
from jargonprofiler.munroe import munroe_score


def test_all_common():
    result = munroe_score("The address of the administration is 1000 green road.",
                          verbose=True)
    assert result["basic_score"] == 100


def test_all_jargon():
    result = munroe_score("epigenetics magic navy")
    assert result["basic_score"] == 0
