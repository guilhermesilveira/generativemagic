import numpy as np

from generativemagic.arrays import np_index
from generativemagic.effect import DECK_TOP, DECK_BOTTOM
from generativemagic.movement import Movement


class ScallopCut(Movement):
    """Cuts to a scalloped, shorted, svengalied card. Simple, perfect cut to a card."""

    def __init__(self, scallop_card: int, cut_to: int = DECK_TOP):
        self._cut_to = cut_to
        self._scallop_card = scallop_card

    def apply(self, sequence, chosen=None):
        position = np_index(sequence, self._scallop_card)
        if self._cut_to == DECK_BOTTOM:
            return np.roll(sequence, len(sequence) - position - 1)
        return np.roll(sequence, -position)

    def __repr__(self):
        return f"ScallopCut({self._scallop_card})"
