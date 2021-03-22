import numpy as np

from random import shuffle


def concatenate(stacks):
    """Concatenates serveral stacks one on top of the other"""
    return np.concatenate(stacks)


def interweave(a, b):
    c = np.empty((a.size + b.size,), dtype=a.dtype)
    c[0::2] = a
    c[1::2] = b
    return c


def revert(deck):
    return np.flip(deck)


def stack_into(stack_count: int, card_count: int, deck, same_stack: bool = False):
    if same_stack:
        stacks = [deck[range(i * stack_count, i * stack_count + card_count)] for i in range(stack_count)]
    else:
        stacks = [deck[range(i, i + stack_count * card_count, card_count)] for i in range(stack_count)]
    remaining = deck[stack_count * card_count:]
    return stacks, remaining


def card_positions_on(deck, x):
    return [i + 1 for i, y in enumerate(deck) if y[:len(x)] == x]


def all_card_sets(deck):
    types = list(map(str, range(2, 10))) + ["ace", "jack", "queen", "king", "ten"]
    return [card_positions_on(deck, t) for t in types]


def all_card_sets_straight():
    return [[i, i + 13, i + 26, i + 39] for i in range(1, 14)]


def all_card_sets_new_deck():
    return [[i, i + 13, 53 - i - 13, 53 - i] for i in range(1, 14)]


def shuffled_copy(ar):
    m = list(ar)
    shuffle(m)
    return m
