import numpy as np

from generativemagic.visualization.combinations import all_compositions_of_fixed_length

BASIC_DECK = [1, 2, 1, 2, 3]
BASIC_DECK_2 = [2, 1, 2, 3, 1]
DECKS = [BASIC_DECK, BASIC_DECK_2]


def test_all_compositions_of_minimal_fixed_length():
    assert dict(all_compositions_of_fixed_length(DECKS, 1)) == {'1': 2, '2': 2, '3': 2}
    assert dict(all_compositions_of_fixed_length(DECKS, 2)) == {'1,2': 2, '2,1': 2, '2,3': 2, '3,1': 1}
    assert dict(all_compositions_of_fixed_length(DECKS, 3)) == {'1,2,1': 1, '2,1,2': 2, '1,2,3': 2, '2,3,1': 1}
    assert dict(all_compositions_of_fixed_length(DECKS, 4)) == {'1,2,1,2': 1, '2,1,2,3': 2, '1,2,3,1': 1}


def test_all_compositions_of_fixed_length():
    assert dict(all_compositions_of_fixed_length(DECKS, 1, 2)) == {'1': 2, '2': 2}
    assert dict(all_compositions_of_fixed_length(DECKS, 2, 2)) == {'1,2': 1}
    assert dict(all_compositions_of_fixed_length(DECKS, 3, 2)) == {}
    assert dict(all_compositions_of_fixed_length(DECKS, 4, 2)) == {}
