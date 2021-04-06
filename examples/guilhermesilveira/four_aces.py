from collections import defaultdict

from generativemagic.effects.four_aces import FourAces, parameter_space, basic_parameter_space2, basic_parameter_space
from generativemagic.effects.hugard_encyclopedia.encyclopedia import SpellingPositionRuler
from generativemagic.mapper import run_parameter_space
from generativemagic.solver.rules import AndRuler
from generativemagic.solver.solver import RuleSolver
from generativemagic.solver.variables import create_card_variables
from generativemagic.spelling import CachedLanguage, Language, English


class FourAcesExample:
    """This effect created by Guilherme Silveira searches for a stacked deck which gives you freedom to execute a SpellingPosition
    effect right after performing a Four Aces effect.

    The magician performs a Four Aces effect, giving a lot of freedom to the
    volunteer. No matter how the deck ends up, we are ready to perform another
    effects. At the end of the final effect you have 8-15 cards face up in any
    order you want, to move on. One could add new effects to it.

    This example shows how z3 solver can be used to find stacked deck positions,
    while still giving a lot of freedom to the volunteers.

    The copyright and performance rights belong to the author."""

    def __init__(self, language: Language):
        self.__language = language

    def fill_card_variables(self):
        all_vars = create_card_variables(self.__language)
        vars_per_length = defaultdict(list)
        for card in all_vars:
            full_name = card.sexpr()
            simple_name = full_name.replace(" ", "")
            vars_per_length[len(simple_name)].append(card)
        return all_vars, vars_per_length

    def run(self, space, extra_ruler=None, card_limiter=None):
        all_vars, vars_per_length = self.fill_card_variables()

        spelling = SpellingPositionRuler(all_vars, vars_per_length, [0, -2, -4], [], card_limiter)

        run_parameter_space(FourAces, space, spelling.create_rule)

        if extra_ruler:
            spelling = AndRuler([spelling, extra_ruler])
            spelling.add_final_rules(all_vars)

        RuleSolver().solve(spelling)


def main():
    language = CachedLanguage(English())
    example = FourAcesExample(language)
    # example.run(basic_parameter_space())
    # example.run(basic_parameter_space2())
    example.run(parameter_space())


if __name__ == '__main__':
    main()
