import logging
from typing import List

from generativemagic.arrays import np_index, cards_positions
from generativemagic.checks.basic import Checker


class IsGenericHand:
    def __init__(self, hands: List[int], can_second_deal: bool, desired_cards):
        self.__hands = hands
        self.__can_second_deal = can_second_deal
        self.__desired_cards = desired_cards

    def check(self, deck):
        for hand in self.__hands:
            found = self.__check_hand(deck, hand)
            if found:
                return hand, found
        return None

    def __check_hand(self, deck, hand):

        positions = cards_positions(deck, self.__desired_cards)

        if -1 in positions:
            # some of the cards were not found
            return None

        length = len(deck)

        for starting in positions:
            len_cards_to_count = len(self.__desired_cards)
            viable_positions = sorted([(starting + i * hand) % length for i in range(len_cards_to_count)])
            if positions == viable_positions:
                return positions

        if not self.__can_second_deal:
            return None

        # this simple O(hand) implementation does not support second dealing with any card, only with the ace
        # it also only supports the required N cards in the first N distributions
        # we can generate all combinations and make this a quick search

        # deltas between each cards
        deltas = [positions[i + 1] - positions[i] - 1 for i in range(len(positions) - 1)]

        # for each but last card
        for position in range(len(deltas) - 1):
            deltas[position] -= hand - 1
            if deltas[position] > 0:
                # too many cards, will have to hold a non ace, fail (could be done, of course)
                return None
            # holding the ace and removing from the next one...
            deltas[position + 1] += deltas[position]
            deltas[position] = 0

        # for the last card
        if deltas[-1] < 0:
            # missing cards before the last ace
            return None
        if deltas[-1] > hand - 1:
            # too many cards before the last one
            return None

        logging.info(positions)
        return positions, deltas


class IsAcesHand(IsGenericHand):
    def __init__(self, hands: List[int], can_second_deal):
        super().__init__(hands, can_second_deal, [1, 14, 27, 40])


class ArePokerHand(Checker):

    def __init__(self, desired, at_start=False):
        self._desired = desired
        self._at_start = at_start

    def check(self, deck):
        positions = cards_positions(deck, [0, 13, 26, 39])
        if self._at_start:
            if positions == [0, 4, 8, 12]:
                return positions
            return None
        l = len(deck)
        for starting in positions:
            if positions == sorted([starting, (starting + 4) % l, (starting + 8) % l, (starting + 12) % l]):
                return positions
        return None

    def __repr__(self):
        return f"ArePokerHand({self._desired},{self._at_start})"
