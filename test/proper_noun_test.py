def proper_noun_in_sentance():
    assert tag_proper_noun("My name is Eilis.") == ["Eilis"]

def proper_noun_begins_sentance():
    assert tag_proper_noun("Eilis is a girl") == ["Eilis"]

def munroe_with_proper_nouns():
    assert munroe_score("Eilis is a small girl") == 75


