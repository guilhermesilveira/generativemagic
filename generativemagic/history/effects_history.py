import logging
from itertools import permutations
from typing import List

from generativemagic.decks import position_to_value, position_to_suit
from generativemagic.mapper import run_parameter_space
from generativemagic.spelling import Language


class Effects:

    def __init__(self, language: Language, sequence: List[int], effects=None, starting=0):
        self._language = language
        self._sequence = sequence
        if not effects:
            effects = []
        self._effects = effects
        self._current = starting
        self._update_values()

    def original_sequence(self):
        return self._sequence

    def _update_values(self):
        self._current_card = int(self._sequence[self._current])
        self._current_value = position_to_value(self._current_card)
        self._current_suit = position_to_suit(self._current_card)

    def current_value(self):
        return self._current_value

    def current_suit(self):
        return self._current_suit

    def move_to_next_card(self):
        if self.has_finished():
            return
        self._current += 1
        if self.has_finished():
            return
        self._update_values()

    def next_two_are(self, a, b):
        if self.is_out_of_bounds(1):
            return False
        following = position_to_value(self._sequence[self._current + 1])
        if self._current_value == a and following == b:
            return True
        if self._current_value == b and following == a:
            return True
        return False

    def next_are(self, *x):
        length = len(x)
        to_analyze = self._sequence[self._current:self._current + length]
        to_remove = list(x)
        for i in to_analyze:
            if i not in to_remove:
                return False
            to_remove.remove(i)
        return True

    def the_next_n_value(self, k):
        if self.is_out_of_bounds(k):
            return 10000
        return position_to_value(self._sequence[self._current + k])

    def the_next_n_suit(self, k):
        if self.is_out_of_bounds(k):
            return 10000
        return position_to_suit(self._sequence[self._current + k])

    def the_next_n_values(self, ks):
        if self.is_out_of_bounds(max(ks)):
            return [-1]
        return [self.the_next_n_value(k) for k in ks]

    def remaining_deck(self):
        return self._sequence[self._current:]

    def next_are_in_and_different(self, k, possible):
        so_far = set()
        for i in range(k):
            checking = self._current + i
            value = position_to_value(self._sequence[checking])
            if value in so_far:
                return False
            if value not in possible:
                return False
            so_far.add(value)
        return True

    def current_position(self):
        return self._current

    def copy(self):
        return Effects(self._language, self._sequence, self._effects.copy(), self._current)

    def description(self):
        return "\n".join(map(str, self._effects))

    def descriptionMD(self):
        return "- " + self.description().replace("\n", "\n- ")

    def append_if(self, card: int, text: str):
        if self.current_value() == card:
            self.append(1, text)
            return True
        return False

    def append(self, quantity, text):
        if self.has_finished():
            return
        pretext = []
        for i in range(quantity):
            pretext.append(f"{self._current_value}," + self._language.card_name(self._current_card))
            self.move_to_next_card()
        text = (pretext, text)
        self._effects.append(text)

    def append_map(self, conditions: dict):
        if self._current_value in conditions:
            self.append(1, conditions[self._current_value])
            return self._current_value
        return None

    def is_out_of_bounds(self, delta):
        return self._current + delta >= len(self._sequence)

    def has_finished(self):
        return self.is_out_of_bounds(0)

    def append_if_suit(self, suit, message):
        if self._current_suit == suit:
            self.append(1, message)
            return True
        return False

    def value_in(self, minimum, maximum):
        return minimum <= self.current_value() <= maximum

    def matches_values(self, values):
        if self.is_out_of_bounds(len(values)):
            return False
        for delta, value in enumerate(values):
            found = self._sequence[self._current + delta]
            if position_to_value(found) != value:
                return False
        return True


def all_possibilities_for(parts, minimum=0, limit_per_part=10000):
    possibilities = []
    max_parts = min(limit_per_part + 1, len(parts) + 1)
    for length in range(minimum, max_parts):
        possibilities.extend(list(permutations(parts, length)))
    logging.debug(f"Calculating for {parts}/{minimum}/{limit_per_part} got {len(possibilities)} possibilities")
    return possibilities


def extract_all_results_from_spelled(results):
    all_results = []
    for result in results:
        current = set()
        for item in result:
            current.add(item[3])
        all_results.extend(current)
    return all_results


def explore_results_of(main_effect, space, deck_creator, effect):
    results = run_parameter_space(main_effect, space, deck_creator=deck_creator)
    logging.info(results[0])
    logging.info(len(results[0]))

    results = list(map(effect.check, results))
    logging.info(results[0])
    return results
