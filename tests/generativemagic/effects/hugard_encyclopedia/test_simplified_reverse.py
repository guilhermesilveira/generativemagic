import numpy as np
from numpy.testing import assert_array_equal

from generativemagic.decks import random_deck
from generativemagic.effect import DECK_TOP, DECK_BOTTOM
from generativemagic.effects.hugard_encyclopedia.simplified_reverse import SimplifiedReverse


def test_put_back_to_top():
    deck = np.random.randint(52)
    assert_array_equal(SimplifiedReverse(DECK_TOP).apply(deck), deck)


def test_put_back_to_bottom():
    deck = random_deck()
    assert_array_equal(SimplifiedReverse(DECK_BOTTOM).apply(deck),
                       np.concatenate([deck[1:], deck[0:1]]))


def test_is_simplified_reverse():
    deck = random_deck()
    assert SimplifiedReverse.is_ready_to_use(deck, deck[0])
    assert SimplifiedReverse.is_ready_to_use(deck, deck[-1])


def test_can_not_simplified_reverse():
    deck = random_deck()
    assert not SimplifiedReverse.is_ready_to_use(deck, deck[1])
