# Copyright and Performance rights by Guilherme Silveira
from itertools import permutations
from typing import List, Tuple
from tqdm import tqdm

import numpy as np
import z3
from z3 import AtMost


def simulate(cuts: Tuple[int], deck: Tuple[int]):
    stacks = np.array([range(cuts[0]),
                       range(cuts[0], cuts[1]),
                       range(cuts[1], cuts[2]),
                       range(cuts[2], 53)])

    return np.concatenate(stacks[[*deck]])


VALUES = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
          "jack", "queen", "king"]
SUITS = ["clubs", "hearts", "spades", "diamonds"]


def retrieve_card_name(position):
    value = (position - 1) % 13
    suit = (position - 1) // 13
    return VALUES[value] + " of " + SUITS[suit]


def rules_all_cards_on_deck(all_vars: List[z3.Int]) -> z3.And:
    rules = [z3.And([card >= 1, card <= 52]) for card in all_vars]
    return z3.And(rules)


def freedom_of_spelling(all_vars: List[z3.Int], cuts: Tuple[int], sequence: Tuple[int]) -> z3.Or:
    deck = simulate(cuts, sequence)
    return spelling_rules(all_vars, deck)


def spelling_rules(all_vars: List[z3.Int], deck: List[int]) -> z3.Or:
    rules = []
    for card in range(1, 53):
        name = retrieve_card_name(card)
        length = len(name.replace(" ", ""))
        original_position = int(deck[length])
        var = all_vars[card - 1]
        rules.append(var == original_position)
        rules.append(var == original_position - 1)
    return z3.Or(rules)


rules = set()
names = map(retrieve_card_name, range(1, 53))
all_vars = list(map(z3.Int, names))

for cut1 in tqdm(range(7, 21)):
    for cut2 in range(max(cut1, 12), 26):
        for cut3 in range(max(cut2, 25), 39):
            for sequence in permutations(range(4)):
                cuts = (cut1, cut2, cut3)
                rule = freedom_of_spelling(all_vars, cuts, sequence)
                rules.add(rule)

for position in range(1, 53):
    at_starting_point = [card == position for card in all_vars]
    rule = AtMost(*at_starting_point, 1)
    rules.add(rule)

rules.add(rules_all_cards_on_deck(all_vars))

print(len(rules))
print(z3.solve(rules))
