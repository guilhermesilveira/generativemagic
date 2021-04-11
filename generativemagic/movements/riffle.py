from typing import List

import numpy as np

from generativemagic.effect import Effect


def riffle_generator(up_to: int, so_far: List = None):
    """Generates all combinations of TOP/BOTTOM/TOP/BOTTOM/etc card mixes up to a certain number"""
    if up_to == 0:
        return

    if not so_far:
        yield from riffle_generator(up_to, [0])
        so_far = []

    remaining = up_to - sum(so_far)
    if remaining == 0:
        yield so_far.copy()
        return

    for i in range(1, remaining + 1):
        so_far.append(i)
        yield from riffle_generator(up_to, so_far)
        so_far.pop()


def basic_parameter_space():
    return [list(riffle_generator(8))]


def parameter_space():
    return [list(riffle_generator(17))]


class RiffleShuffle(Effect):

    def __init__(self, interest: List[int]):
        self._interest = interest

    def apply(self, sequence: np.array, chosen=None):
        result = []
        is_right = 0
        positions = [0, 26]
        for amount in self._interest:
            at = positions[is_right]
            result.extend(sequence[at:at + amount])
            positions[is_right] += amount
            is_right = 1 - is_right
        return np.concatenate([result, sequence[positions[0]:26], sequence[positions[1]:]])

    def __repr__(self):
        return f"RiffleShuffle({self._interest})"
