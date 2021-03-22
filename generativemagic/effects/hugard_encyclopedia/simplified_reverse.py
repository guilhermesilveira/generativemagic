import numpy as np

from generativemagic.decks import is_int_card
from generativemagic.effect import Effect, DECK_TOP


class IsSimplifiedReverse:
    def check(self, deck, chosen):
        if not is_int_card(chosen):
            return None
        return deck[0] == chosen or deck[-1] == chosen


class SimplifiedReverse(Effect):
    """A (chosen) card on top of the deck is found reversed in the middle of the deck."""

    def __init__(self, put_back_on):
        self.__put_back_on = put_back_on

    def apply(self, sequence):
        if self.__put_back_on == DECK_TOP:
            return sequence
        return np.roll(sequence, -1)

    def __repr__(self):
        return f"SimplifiedReverse({self.__put_back_on})"

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        return IsSimplifiedReverse().check(deck, chosen)
