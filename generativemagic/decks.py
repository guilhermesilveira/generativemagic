import numpy as np

SUIT_CLUBS = 0
SUIT_HEARTS = 1
SUIT_SPADES = 2
SUIT_DIAMONDS = 3
ACE = 1
JACK = 11
QUEEN = 12
KING = 13


def simple_deck():
    """A deck Ace to King. This is NOT the united statess based new deck order!"""
    return np.arange(1, 53)


def random_deck():
    """A random deck"""
    return np.random.permutation(52) + 1


def position_to_value(k: int):
    assert 0 < k < 53
    return (k - 1) % 13 + 1


def position_to_suit(k):
    assert 0 < k < 53
    return int((k - 1) / 13)


def position_to_suit_color(k):
    assert 0 < k < 53
    return int((k - 1) / 13) % 2


def value_and_suit_to_card(value, suit):
    assert 0 < value < 14 and 0 <= suit <= 3
    return suit * 13 + value


def value_and_suit_to_card_position_on_simple_deck(value, suit):
    return value_and_suit_to_card(value, suit) - 1


def is_int_card(card):
    return isinstance(card, (int, np.integer))
