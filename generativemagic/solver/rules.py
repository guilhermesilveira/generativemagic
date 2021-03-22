from collections import Iterable

from z3 import And


def rules_aces_on_top(all_vars):
    """Returns 4 rules so that all aces are on the top 4 positions"""

    aces = [all_vars[0], all_vars[13], all_vars[26], all_vars[39]]
    return list(map(rule_card_on_top_4, aces))


def rule_card_on_top_4(var_card):
    """Returns one rule so that the card is on one of the top 4 positions"""

    # 24k => test_aces 234 secs
    return And(var_card >= 1, var_card <= 4)
    # 24k => test_aces(1) 1000 secs with OR!!!!!!
    # return Or(var_card == 1, var_card == 2, var_card == 3, var_card == 4)


def rules_all_cards_on_deck(all_vars):
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

    def add_final_rules(self, all_vars):
        self.__rules = [rules_all_cards_on_deck(all_vars)]


class Ruler:

    def rules(self) -> Iterable:
        pass

    def create_rule(self, x, deck):
        pass

    def add_final_rules(self, all_vars):
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
