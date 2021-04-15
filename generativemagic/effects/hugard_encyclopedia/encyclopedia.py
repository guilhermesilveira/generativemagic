import logging

import numpy as np
from z3 import Or, AtMost

from generativemagic.deck_operations import concatenate
from generativemagic.decks import SUIT_CLUBS, SUIT_HEARTS, SUIT_SPADES, SUIT_DIAMONDS, value_and_suit_to_card, \
    position_to_value
from generativemagic.effect import Effect
from generativemagic.solver.rules import Ruler, rules_aces_on_top


class TheMagicBreath(Effect):
    def __init__(self, n: int, put_stack_back_on_top=True, put_chosen_card_on_bottom=False):
        self.n = n
        self.put_stack_back_on_top = put_stack_back_on_top
        self.put_chosen_card_on_bottom = put_chosen_card_on_bottom

    def movements_description(self):
        return [["count", "n"], ["count", "n"],
                ["put back to bottom or top", "put_stack_back_on_top"],
                ["put_chosen_card_on_bottom", "put_chosen_card_on_bottom"]]

    def apply(self, sequence):
        if self.put_stack_back_on_top:

            if self.put_chosen_card_on_bottom:
                return np.roll(sequence, -1)

            return sequence

        if self.put_chosen_card_on_bottom:
            return concatenate([sequence[:self.n], sequence[self.n:], [sequence[0]]])

        return np.roll(sequence, -self.n)

    def __repr__(self):
        return f"TheMagicBreath({self.n},put_stack_back_on_top={self.put_stack_back_on_top},put_chosen_card_on_bottom={self.put_chosen_card_on_bottom})"


class PhenomenalThoughtCardsRuler(Ruler):
    """The Phenomenal Thought Cards effect allows the volunteer to pick a random card,
    put on the middle of the deck. The magician goes through the cards face down, until the magician says
    I have found it.

    That is not the chosen card, for example it is a 5. So now the magician says, well, five right?
    One, two, three, four, five (counts to the card), and there is the selected card.

    For this Ruler variation of the effect to work you need all number cards that can be used
    as counters to be marked because you don't know which one it will be until showtime. The possible
    cards is the *possible_cards* argument, which defaults to [7, 8 and 9]."""

    def __init__(self, all_vars, possible_cards=None):
        self.__all_vars = all_vars
        self.__rules = []
        if possible_cards:
            self.__possible_cards = possible_cards
        else:
            self.__possible_cards = [7, 8, 9]

    def create_rule(self, _, deck_order):
        conditions = []
        for value in self.__possible_cards:
            card_1_at_position = deck_order[-value]
            card_2_at_position = deck_order[value]
            cards = [value_and_suit_to_card(value, SUIT_CLUBS),
                     value_and_suit_to_card(value, SUIT_HEARTS),
                     value_and_suit_to_card(value, SUIT_SPADES),
                     value_and_suit_to_card(value, SUIT_DIAMONDS)]
            conditions.extend(list(map(lambda card: self.__all_vars[card] == card_1_at_position.item(), cards)))
            conditions.extend(list(map(lambda card: self.__all_vars[card] == card_2_at_position.item(), cards)))
        self.__rules.append(Or(conditions))

    def add_final_rules(self, all_vars):
        logging.info(f"{len(self.__rules)} generated rules")

    def rules(self):
        return self.__rules

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        for count in [7, 8, 9]:
            for position in [-count, count]:
                if position_to_value(deck[position]) == count:
                    return [[count], [position, position_to_value(deck[position]), deck[position]]]
        return None
