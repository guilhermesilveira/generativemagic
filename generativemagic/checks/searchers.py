import logging
from asyncio import Queue
from queue import SimpleQueue
from typing import List, Callable, NewType, Generator, Tuple, Dict

import numpy as np

from generativemagic.decks import simple_deck
from generativemagic.movement import Reorder
from generativemagic.spelling import English
import pandas as pd

ValidationFunction = NewType("ValidationFunction", Callable[[List[int]], bool])
Deck = NewType("Deck", np.array)
LimiterCallback = NewType("LimiterCallback", Callable[[int], bool])


def depth_limiter(k):
    """A limiter on depth k"""
    return lambda depth: depth >= k


def no_limit(depth):
    """No limit on depth"""
    return False


SpaceCombination = NewType("SpaceCombination", Tuple[Deck, List, int])


class Searcher:

    def __init__(self, all_movements: List, extra_limiter: Callable = None):
        self.all_movements = all_movements
        self.extra_limiter = extra_limiter

    def _non_limiting(self, depth):
        return False

    def _bfs_search(self, starting_deck: Deck,
                    validating_function: ValidationFunction,
                    limiter: LimiterCallback):
        valid = validating_function(starting_deck)
        if valid:
            print(f"FOUND IT!! 0")
            return starting_deck, [], valid

        decks_to_evaluate = SimpleQueue()
        decks_to_evaluate.put((starting_deck, [], 0))

        parsed = 0

        while not decks_to_evaluate.empty():

            deck, used, depth = decks_to_evaluate.get()
            if limiter(depth):
                return None

            for movement in self.all_movements:
                if movement in used:
                    continue

                # TODO do not use those global limits
                if not movement.still_can_use(used):
                    continue

                if self.extra_limiter and not self.extra_limiter(movement, used):
                    continue

                resulting_used = used.copy()
                resulting_used.append(movement)

                resulting_deck = movement.apply(deck)
                valid = validating_function(resulting_deck)

                if valid:
                    print(f"FOUND IT!! {depth + 1}")
                    return resulting_deck, resulting_used, valid

                decks_to_evaluate.put(([resulting_deck, resulting_used, depth + 1]))
                parsed += 1

                if parsed % 5000 == 0:
                    msg = ",".join([f"{resulting_deck[10:16]}"]) + ":" + str(depth + 1) + ":" + str(
                        valid)
                    logging.info(f"{parsed} parsed: " + msg)

        return None

    def search(self, starting_deck: Deck,
               validating_function: ValidationFunction,
               limiter: LimiterCallback = no_limit):
        logging.info(f"Starting search with total of #{len(self.all_movements)} movements")
        return self._bfs_search(starting_deck,
                                validating_function,
                                limiter)


def limit_search(validation: ValidationFunction,
                 deck: Deck = None,
                 limits=(1, 2, 3, 4),
                 searcher=None,
                 movements=None):
    if searcher is None:
        searcher = Searcher(movements.values())
    if deck is None:
        deck = simple_deck()

    for limit in limits:
        print(f"Checking limit={limit}")
        result = searcher.search(deck, validation, depth_limiter(limit))
        if result is not None:
            current_deck, used_so_far, valid = result
            print(f"limit {limit} SUCCESS:")
            print(result)
            print(current_deck)
            print(used_so_far)
            print(valid)
            print()
            return True

    return False


class TypeLimiter:
    def __init__(self):
        self.limiters = {}

    def limit(self, who, quantity):
        self.limiters[who] = quantity
        return self

    def check(self, movement, used_so_far):
        if type(movement) != Reorder:
            return True
        # print(self.limiters, movement.simple_name, movement.simple_name not in self.limiters)
        if movement.simple_name not in self.limiters:
            return True
        count = 0
        # print(f"{movement} might be limited")
        for used in used_so_far:
            if movement.simple_name in used.name():
                count += 1
                if count >= self.limiters[movement.simple_name]:
                    # print(f"Limiting {movement} because {used_so_far}")
                    return False
        return True


def simulate(steps, deck):
    ds = []
    for i, step in enumerate(steps):
        before_deck = deck
        deck = step.apply(deck)
        ds.append([i, step, before_deck, deck.tolist(), English().name_of_deck(deck)])
        print(i, deck)
    return pd.DataFrame(ds, columns=["i", "step", "before_deck", "after_deck", "new_mnemonica_simple_deck"])
    # print(name_of_deck(deck))

# def try_all_limits(deck, limits, divination):
#     print(f"\n\n4 ANY limit {limits} {divination}")
#     limit_search(AreKSetCardsTogether(4, all_card_sets_new_deck).check, deck=deck, limits=limits)
