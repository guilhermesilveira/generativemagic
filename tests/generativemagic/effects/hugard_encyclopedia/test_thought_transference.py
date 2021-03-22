import numpy as np
from numpy.testing import assert_array_equal

from generativemagic.effects.hugard_encyclopedia.thought_transference import ORIGINAL, ThoughtTransference, \
    REVERT_COMPLETELY, REVERT_ROWS


def test_return_to_original_order():
    deck = np.random.randint(52)

    assert_array_equal(ThoughtTransference(3, ORIGINAL).apply(deck), deck)


def test_revert_completely():
    deck = np.arange(1, 10)
    assert_array_equal(ThoughtTransference(2, REVERT_COMPLETELY).apply(deck), [4, 3, 2, 1, 5, 6, 7, 8, 9])


def test_revert_rows():
    deck = np.arange(1, 10)
    assert_array_equal(ThoughtTransference(2, REVERT_ROWS).apply(deck), [3, 4, 1, 2, 5, 6, 7, 8, 9])
