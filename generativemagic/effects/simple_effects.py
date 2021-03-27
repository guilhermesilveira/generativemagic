import numpy as np

from generativemagic.effect import Effect, DECK_TOP


class InjectAt(Effect):
    """Injects a chosen cards at the top or bottom of the deck.
    This is a simple palming or putting the deck on top of the chosen cards.

    Why does it not allow to put anywhere? Because this is a simple movement to put on top or bottom."""

    def __init__(self, at: int):
        self.__at = at

    def apply(self, sequence, chosen=None):
        if self.__at == DECK_TOP:
            return np.insert(sequence, 0, chosen)
        return np.insert(sequence, len(sequence), chosen)

    def __repr__(self):
        return f"InjectAt({self.__at})"
