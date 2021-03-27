import numpy as np
from numpy.testing import assert_array_equal

from generativemagic.decks import simple_deck
from generativemagic.effect import DECK_TOP, DECK_BOTTOM
from generativemagic.effects.simple_effects import InjectAt


def test_inject_at_top():
    deck = [1, 2, 3, 4]
    assert_array_equal(InjectAt(DECK_TOP).apply(deck, 15), [15, 1, 2, 3, 4])


def test_inject_multiple():
    deck = [1, 2, 3, 4]
    assert_array_equal(InjectAt(DECK_TOP).apply(deck, [15, 13]), [15, 13, 1, 2, 3, 4])


def test_inject_at_bottom():
    deck = simple_deck()
    print(len(deck))
    assert_array_equal(InjectAt(DECK_BOTTOM).apply(deck, -1), np.append(simple_deck(), -1))
