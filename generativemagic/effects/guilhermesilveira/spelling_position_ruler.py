import logging
from typing import List

import z3
from z3 import Or, AtMost, Int

from generativemagic.solver.rules import Ruler, rules_aces_on_top


class SpellingPositionRuler(Ruler):
    def __init__(self, all_vars, vars_per_length,
                 deltas_from_top=None,
                 deltas_from_bottom=None,
                 supports_next=False,
                 card_limiter=lambda c: True):
        self._supports_next = supports_next
        self._card_limiter = card_limiter
        self.__all_vars = all_vars
        self._positions = {}
        for i, card in enumerate(all_vars, start=1):
            self._positions[card] = i
        self.vars_per_length = vars_per_length
        if deltas_from_bottom is None:
            deltas_from_bottom = []
        self.deltas_from_bottom = deltas_from_bottom
        if deltas_from_top is None:
            deltas_from_top = []
        self.deltas_from_top = deltas_from_top
        self.__rules = set()
        self.used_positions = {1, 2, 3, 4}

    def create_rule(self, _, deck_order):
        all_ors = []
        for current_length in self.vars_per_length.keys():
            for original_card in self.vars_per_length[current_length]:
                if self._card_limiter and not self._card_limiter(self._positions[original_card]):
                    continue
                for delta in self.deltas_from_top:
                    self._position(deck_order[current_length - 1 + delta], all_ors, original_card)
                    if self._supports_next:
                        self._position(deck_order[current_length + delta], all_ors, original_card)
                for delta in self.deltas_from_bottom:
                    self._position(deck_order[- current_length - delta], all_ors, original_card)
                    if self._supports_next:
                        self._position(deck_order[- current_length - delta - 1], all_ors, original_card)
        all_ors = Or(all_ors)
        self.__rules.add(all_ors)

    def __add_rules_for_cards_must_be_in_deck(self, all_vars):
        for r in rules_aces_on_top(all_vars):
            self.__rules.add(r)

        for c in self.used_positions:
            all_conditions = [card == c for card in all_vars]
            self.__rules.add(AtMost(*all_conditions, 1))
        logging.info(f"{len(self.used_positions)} used positions: {self.used_positions}")
        logging.info(f"{len(self.__rules)} generated rules")

    def add_final_rules(self, all_vars):
        self.__add_rules_for_cards_must_be_in_deck(all_vars)

    def rules(self):
        return list(self.__rules)

    def _position(self, card_number, all_ors: List, card: z3.Int):
        card_int = card_number.item()
        self.used_positions.add(card_int)
        all_ors.append(card == card_int)
