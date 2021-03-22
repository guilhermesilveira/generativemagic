import numpy as np

from generativemagic.movement import Movement


class TopToBottom(Movement):
    def __init__(self, n):
        self.n = n

    def apply(self, sequence, chosen=None):
        return np.roll(sequence, -self.n)

    def __repr__(self):
        return f"TopToBottom({self.n})"


class BottomToTop(Movement):
    def __init__(self, n):
        self.n = n

    def apply(self, sequence, chosen=None):
        return np.roll(sequence, self.n)

    def __repr__(self):
        return f"BottomToTop({self.n})"


class TopToLastToBottom(Movement):
    """Draw two cards from the deck in a simple motion, put them at the bottom of the deck."""

    def apply(self, sequence, chosen=None):
        return np.append(sequence[1:-1], [sequence[0], sequence[-1]])

    def __repr__(self):
        return f"TopToLastToBottom()"


class BottomToSecond(Movement):
    """Draw two cards from the deck in a simple motion, put them at the top of the deck."""

    def apply(self, sequence, chosen=None):
        return np.insert(sequence[:-1], 1, sequence[-1])

    def __repr__(self):
        return f"BottomToSecond()"
