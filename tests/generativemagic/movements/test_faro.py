import numpy as np

from numpy.testing import assert_array_equal
from generativemagic.movements.faro import InFaro, OutFaro

FOUR_CARDS_DECK = np.array([1, 2, 3, 4])


def test_in_faros():
    series = [[3, 1, 4, 2],
              [4, 3, 2, 1],
              [2, 4, 1, 3],
              [1, 2, 3, 4]]
    deck = FOUR_CARDS_DECK
    for expected in series:
        deck = InFaro().apply(deck)
        assert_array_equal(deck, expected)


def test_out_faros():
    series = [[1, 3, 2, 4],
              [1, 2, 3, 4]]
    deck = FOUR_CARDS_DECK
    for expected in series:
        deck = OutFaro().apply(deck)
        assert_array_equal(deck, expected)
