from collections import Iterable
from typing import List

from z3 import And, Or, Int


def rules_aces_on_top(all_vars: List[Int]):
    """Returns 4 rules so that all aces are on the top 4 positions"""

    aces = [all_vars[0], all_vars[13], all_vars[26], all_vars[39]]
    return list(map(rule_card_on_top_4, aces))


def rule_card_on_top_4(var_card: Int):
    """Returns one rule so that the card is on one of the top 4 positions"""

    # 24k => test_aces 234 secs
    return And(var_card >= 1, var_card <= 4)
    # 24k => test_aces(1) 1000 secs with OR!!!!!!
    # return Or(var_card == 1, var_card == 2, var_card == 3, var_card == 4)


def rules_all_cards_on_deck(all_vars: List[Int]):
    """Returns 52 cards must be on deck"""
    rules = []
    for var_card in all_vars:
        rules.append(var_card >= 1)
        rules.append(var_card <= 52)
    return And(rules)


class AllCardsOnDeck:
    """Left over as a non recommendation to use. Adding extra rules will make things slower.
    If they can get random values, that will be ok."""

    def __init__(self):
        self.__rules = []

    def rules(self) -> Iterable:
        return self.__rules

    def add_final_rules(self, all_vars: List[int]):
        self.__rules = [rules_all_cards_on_deck(all_vars)]


class Ruler:

    def rules(self) -> Iterable:
        pass

    def create_rule(self, x, deck):
        pass

    def add_final_rules(self, all_vars: List[int]):
        pass


class AndRuler(Ruler):
    def __init__(self, rulers):
        self.__rulers = rulers

    def create_rule(self, x, deck):
        for ruler in self.__rulers:
            ruler.create_rule(x, deck)

    def add_final_rules(self, all_vars):
        for ruler in self.__rulers:
            ruler.add_final_rules(all_vars)

    def rules(self):
        all_rules = []
        for ruler in self.__rulers:
            all_rules.extend(ruler.rules())
        return all_rules


def add_sequential_condition(firsts, seconds, all_vars):
    """all of the first must be followed by one of the seconds"""
    rules = []
    for first in firsts:
        possibles = []
        first_var = all_vars[first - 1]
        for second in seconds:
            second_var = all_vars[second - 1]
            possibles.append(first_var == (second_var + 1))
        rules.append(Or(possibles))
    return rules


def not_on_border(elements: List[int], all_vars,
                  can_be_on_first: bool = False,
                  can_be_on_last: bool = False):
    """all of the elements must not be in the border"""
    rules = []
    for element in elements:
        var = all_vars[element - 1]
        if not can_be_on_first:
            rules.append(var >= 2)
        if not can_be_on_last:
            rules.append(var <= 51)
    return rules


def on_deck(elements: List[int], all_vars):
    """all of the elements must be within the deck"""
    rules = []
    for element in elements:
        var = all_vars[element - 1]
        rules.append(var >= 1)
        rules.append(var <= 52)
    return rules
