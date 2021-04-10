from itertools import permutations

import numpy as np

from generativemagic.deck_operations import concatenate
from generativemagic.effect import Effect
from generativemagic.mapper import EffectInvalidParameterError


def global_parameter_space():
    """This parameter space is unnecessarily too large"""
    return [list(range(7, 22)),
            list(range(12, 27)),
            list(range(25, 40)),
            list(permutations(range(1, 5)))]


def parameter_space():
    """This is a good parameter space as you spread the cards in your hands or go over them with your fingers.
    Remember to control the starting point by calling the next volunteer to say stop. The stop point by hiding 
    the cards with your other hand."""
    return [list(range(7, 17)),
            list(range(17, 27)),
            list(range(27, 37)),
            list(permutations(range(1, 5), 4))]


def basic_parameter_space2():
    return [list(range(9, 15)),
            list(range(15, 21)),
            list(range(21, 27)),
            list(permutations(range(1, 5), 4))]


def basic_parameter_space():
    return [list(range(9, 15)),
            list(range(15, 19)),
            list(range(19, 26)),
            list(permutations(range(1, 5), 4))]


class FourAces(Effect):
    """Can be improved by limiting the number of choices of the user, if required."""

    def __init__(self, cut_point_0, cut_point_1, cut_point_2, sorting_order):
        if cut_point_0 >= cut_point_1 or cut_point_1 >= cut_point_2:
            raise EffectInvalidParameterError
        self.cut_points = [cut_point_0, cut_point_1, cut_point_2]
        self.sorting_order = sorting_order

    def apply(self, sequence):
        p0 = sequence[:4]
        p1 = sequence[4:self.cut_points[0]]
        p2 = sequence[self.cut_points[0] + 1:self.cut_points[1]]
        p3 = sequence[self.cut_points[1] + 1:self.cut_points[2]]
        p4 = sequence[self.cut_points[2]:]
        p4 = concatenate([[sequence[self.cut_points[0]], sequence[self.cut_points[1]]], p4])
        ps = np.array([p0, p1, p2, p3, p4], dtype=object)

        # removed the 4 top cards
        return concatenate(ps[[*self.sorting_order]])

    def __repr__(self):
        return f"FourAces({self.cut_points},{self.sorting_order})"

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        aces_on_top = [card for card in deck[:4] if card in [0, 13, 26, 39]]
        if len(aces_on_top) == 4:
            return True
        return None
