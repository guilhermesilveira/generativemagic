import numpy as np

from generativemagic.effect import Effect, DECK_TOP


class SagaciousJokerN1(Effect):
    """> Sagacious Joker N1, Jordan
> N cards are selected, their suit or color are revealed
> Sagacious Joker N2 is very similar
- Result: N cards plus the top card are displaced to the top or bottom
- Requires N people with pockets"""

    def __init__(self, selections: list, put_back_at):
        self._put_back_at = put_back_at
        self._selections = selections

    def apply(self, sequence, chosen=None):
        without = np.array([x for x in sequence if x not in self._selections])
        if self._put_back_at == DECK_TOP:
            return np.concatenate([self._selections, without])
        return np.concatenate([without, self._selections])

    def __repr__(self):
        return f"SagaciousJokerN1()"

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        return True
