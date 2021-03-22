import numpy as np

from generativemagic.effect import Effect

REVERT_COMPLETELY = "REVERT_COMPLETELY"
ORIGINAL = "ORIGINAL"
REVERT_ROWS = "REVERT_ROWS"


class ThoughtTransference(Effect):
    """A NxN matrix based one card prediction."""

    def __init__(self, n, returning_order=None):
        self.__returning_order = returning_order
        if not self.__returning_order:
            self.__returning_order = REVERT_COMPLETELY
        self.__n = n

    def apply(self, sequence):

        if self.__returning_order == REVERT_COMPLETELY:
            return np.concatenate([sequence[self.__n ** 2 - 1::-1], sequence[self.__n ** 2:]])

        if self.__returning_order == ORIGINAL:
            return sequence

        rows = list(reversed([sequence[i * self.__n:(i + 1) * self.__n] for i in range(self.__n)]))
        rows.append(sequence[self.__n ** 2:])
        return np.concatenate(rows)

    def __repr__(self):
        return f"ThoughtTransference({self.__n},{self.__returning_order})"

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        return True
