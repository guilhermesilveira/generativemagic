import numpy as np

from numpy.testing import assert_array_equal

from generativemagic.effect import DECK_BOTTOM
from generativemagic.movements.scallop import ScallopCut

FOUR_CARDS_DECK = np.array([1, 3, 2, 4])


def test_scallop_to_top():
    assert_array_equal(ScallopCut(1).apply(FOUR_CARDS_DECK), [1, 3, 2, 4])
    assert_array_equal(ScallopCut(2).apply(FOUR_CARDS_DECK), [2, 4, 1, 3])
    assert_array_equal(ScallopCut(3).apply(FOUR_CARDS_DECK), [3, 2, 4, 1])
    assert_array_equal(ScallopCut(4).apply(FOUR_CARDS_DECK), [4, 1, 3, 2])


def test_scallop_to_bottom():
    assert_array_equal(ScallopCut(4, DECK_BOTTOM).apply(FOUR_CARDS_DECK), [1, 3, 2, 4])
    assert_array_equal(ScallopCut(3, DECK_BOTTOM).apply(FOUR_CARDS_DECK), [2, 4, 1, 3])
    assert_array_equal(ScallopCut(1, DECK_BOTTOM).apply(FOUR_CARDS_DECK), [3, 2, 4, 1])
    assert_array_equal(ScallopCut(2, DECK_BOTTOM).apply(FOUR_CARDS_DECK), [4, 1, 3, 2])
