from numpy import argmin

from generativemagic.checks.poker import cards_positions
from generativemagic.decks import value_and_suit_to_card, SUIT_CLUBS, SUIT_HEARTS
from generativemagic.effect import Effect

THREE_CLUBS = value_and_suit_to_card(3, SUIT_CLUBS)
THREE_HEARTS = value_and_suit_to_card(3, SUIT_HEARTS)
TWO_CLUBS = value_and_suit_to_card(2, SUIT_CLUBS)
REQUIRED_CARDS = [THREE_CLUBS, THREE_HEARTS, TWO_CLUBS]


class IsTrucoHand:
    def __init__(self, hands, can_second_deal):
        self.__can_second_deal = can_second_deal
        self.__hands = hands

    def check(self, deck):
        for hand in self.__hands:
            found = self.__check_hand(deck, hand)
            if found:
                return hand, found
        return None

    def __check_hand(self, deck, hand):
        positions = cards_positions(deck, REQUIRED_CARDS)
        maximum_delta = hand * 3 + 1

        if self.__can_second_deal:
            maximum_delta += 1

        length = len(REQUIRED_CARDS)
        distances = []
        for i in range(length):
            first = positions[i]
            last = positions[(i + length - 1) % length]
            distance = last - first
            if distance < 0:
                distance += len(deck)
            distance += 1
            distances.append(distance)

        minimum_arg = argmin(distances)
        print(positions, maximum_delta, distances, minimum_arg)
        if distances[minimum_arg] <= maximum_delta:
            return {
                "minimum distance": distances[minimum_arg],
                "position": positions[minimum_arg],
                "positions": positions
            }

        return None


class TrucoHand(Effect):

    def apply(self, sequence):
        result = IsTrucoHand([2, 4], True).get_first_ace(sequence)
        raise Exception(f"To be implemented at {result}")

    def __repr__(self):
        return f"AcesHand()"

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        return IsTrucoHand([2, 4], True).check(deck)
