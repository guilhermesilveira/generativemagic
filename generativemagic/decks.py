from typing import NewType

import numpy as np

Deck = NewType("Deck", np.array)

SUIT_CLUBS = 0
SUIT_HEARTS = 1
SUIT_SPADES = 2
SUIT_DIAMONDS = 3
ACE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
JACK = 11
QUEEN = 12
KING = 13

TWOS = [2, 2 + 13, 2 + 26, 2 + 39]
THREES = [3, 3 + 13, 3 + 26, 3 + 39]
FOURS = [4, 4 + 13, 4 + 26, 4 + 39]
FIVES = [5, 5 + 13, 5 + 26, 5 + 39]
SIXES = [6, 6 + 13, 6 + 26, 6 + 39]
EIGHTS = [8, 8 + 13, 8 + 26, 8 + 39]
NINES = [9, 9 + 13, 9 + 26, 9 + 39]
QUEENS = [12, 12 + 13, 12 + 26, 12 + 39]
KINGS = [13, 13 + 13, 13 + 26, 13 + 39]


def simple_deck():
    """A deck Ace to King. This is NOT the united statess based new deck order!"""
    return np.arange(1, 53)


def random_deck():
    """A random deck"""
    return np.random.permutation(52) + 1


def position_to_value(k: int) -> int:
    assert 0 < k < 53
    return (k - 1) % 13 + 1


def position_to_suit(k: int) -> int:
    assert 0 < k < 53
    return int((k - 1) / 13)


def position_to_suit_color(k: int):
    assert 0 < k < 53
    return int((k - 1) / 13) % 2


def value_and_suit_to_card(value: int, suit: int):
    assert 0 < value < 14 and 0 <= suit <= 3
    return suit * 13 + value


def value_and_suit_to_card_position_on_simple_deck(value: int, suit: int):
    return value_and_suit_to_card(value, suit) - 1


def is_int_card(card: int):
    return isinstance(card, (int, np.integer))


def deck_as_str(sequence):
    """Returns a deck as a string"""
    return ",".join(map(str, sequence))
