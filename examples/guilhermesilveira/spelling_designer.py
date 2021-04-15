from collections import defaultdict
from typing import List

from generativemagic.effects.guilhermesilveira.spelling_position_ruler import SpellingPositionRuler
from generativemagic.mapper import run_parameter_space
from generativemagic.solver.rules import AndRuler
from generativemagic.solver.solver import RuleSolver
from generativemagic.solver.variables import create_card_variables
from generativemagic.spelling import Language


def get_vars_per_length(all_vars: List, names: List) -> defaultdict:
    vars_per_length = defaultdict(list)
    for card, full_name in zip(all_vars, names):
        simple_name = full_name.replace(" ", "")
        vars_per_length[len(simple_name)].append(card)
    return vars_per_length


class SpellingDesigner:
    """This effect created by Guilherme Silveira searches for a stacked deck which gives
    the magician freedom to execute a SpellingPosition effect right after performing a Four Aces effect.

    The magician performs a Four Aces effect, giving a lot of freedom to the
    volunteer. No matter how the deck ends up, we are ready to perform another
    effects. At the end of the final effect you have 8-15 cards face up in any
    order you want, to move on. One could add new effects to it.

    This example shows how z3 solver can be used to find stacked deck positions,
    while still giving a lot of freedom to the volunteers.

    The copyright and performance rights belong to the author."""

    def __init__(self, language: Language):
        self.__language = language
        self.all_vars, self.vars_per_length = self._fill_card_variables()

    def _fill_card_variables(self):
        all_vars, names = create_card_variables(self.__language)
        vars_per_length = get_vars_per_length(all_vars, names)
        return all_vars, vars_per_length

    def run(self, space, effect_type,
            extra_rulers=None,
            card_limiter=None,
            supports_next=False,
            threads=1):
        spelling = SpellingPositionRuler(self.all_vars, self.vars_per_length,
                                         deltas_from_top=[0, -2, -4],
                                         supports_next=supports_next,
                                         deltas_from_bottom=[],
                                         card_limiter=card_limiter)
        run_parameter_space(effect_type, space, spelling.create_rule, threads=threads)

        if extra_rulers:
            spelling = AndRuler([spelling] + extra_rulers)

        spelling.add_final_rules(self.all_vars)

        RuleSolver().solve(spelling)
