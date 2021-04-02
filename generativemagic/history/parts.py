from collections import Counter

from tqdm import tqdm

from generativemagic.history.effects_history import Effects, all_possibilities_for
from generativemagic.spelling import Language
import logging


class PartsStructure:
    def explore(self, all_effects: dict, prune=52, limit_per_part=10000):
        raise Exception(f"Parts exploration must be implemented on {type(self)}")


class SimpleParts(PartsStructure):
    def __init__(self, parts, minimum=0, maximum=None):
        self._maximum = maximum
        self._minimum = minimum
        self._parts = parts

    def explore(self, all_effects: dict, prune=52, limit_per_part=10000):
        # ugly, improve it
        if self._maximum:
            limit_per_part = self._maximum
        possibilities = all_possibilities_for(self._parts, self._minimum, limit_per_part)

        temp_all_effects = self.create_temporary_list_of_effects_so_far(all_effects)

        largest_position = 1
        for effects in all_effects.values():

            # prune optimization
            if largest_position - effects.current_position() > prune:
                continue

            snapshot = effects.copy()
            for possibility in possibilities:
                effects = snapshot.copy()
                for story in possibility:
                    story(effects)
                    if effects.has_finished():
                        return effects

                # prune optimization
                if largest_position > effects.current_position() and \
                        largest_position - effects.current_position() > prune:
                    continue

                current = effects.current_position()

                exists = current in temp_all_effects
                if not exists:
                    temp_all_effects[current] = effects
                    largest_position = max(largest_position, current)

        return temp_all_effects

    def create_temporary_list_of_effects_so_far(self, all_effects):
        return all_effects.copy()


class AtLeastOnePart(SimpleParts):
    """Only effects that include at least one of these parts will be accepted"""

    def __init__(self, parts, minimum=1, maximum=None):
        super().__init__(parts, minimum, maximum)

    def create_temporary_list_of_effects_so_far(self, all_effects):
        return {}


class Optional(PartsStructure):
    def __init__(self, part):
        if type(part) is list:
            raise Exception("Only a single part can be optional")
        self._part = part

    def explore(self, all_effects: dict, prune=52, limit_per_part=10000):
        return SimpleParts([self._part]).explore(all_effects, prune, limit_per_part)


class OrParts(PartsStructure):
    def __init__(self, parts):
        super().__init__(parts)

    def explore(self, all_effects: dict, prune=52, limit_per_part=10000):
        for sub_parts in self._parts:
            result = _explore(sub_parts, all_effects, prune, limit_per_part)
            if type(result) == Effects:
                return result
            if result != all_effects:
                return result
        return all_effects


def _explore(parts, all_effects: dict, prune=52, limit_per_part=10000):
    if type(parts) == list:
        return SimpleParts(parts).explore(all_effects, prune, limit_per_part)
    return parts.explore(all_effects, prune, limit_per_part)


class Parts:
    def __init__(self):
        self._parts = []

    def add(self, custom_part):
        self._parts.append(custom_part)
        return self

    def optional(self, part):
        return self.add(Optional(part))

    def mandatory(self, part):
        return self.add(AtLeastOnePart([part]))

    def parts(self) -> list:
        return self._parts.copy()

    def quantity(self, minimum, maximum, parts):
        return self.add(AtLeastOnePart(parts, minimum=minimum, maximum=maximum))

    def at_least_one(self, parts):
        return self.add(AtLeastOnePart(parts, minimum=1))


def explore_all(language: Language, sequence: list, all_parts: list,
                prune: int = 1000, limit_per_part=10) -> Effects:
    base_effects = Effects(language, sequence)
    all_effects = {0: base_effects}

    logging.info(f"Exploring all parts {all_parts}")

    for parts in all_parts:

        logging.debug(f"Going for parts {parts}")
        result = _explore(parts, all_effects,
                          prune=prune, limit_per_part=limit_per_part)
        if type(result) == Effects:
            return result

        all_effects = result

    return find_best_effect(all_effects)


def find_best_effect(all_effects: dict) -> Effects:
    if type(all_effects) != dict:
        raise Exception(f"All effects should be a dict, got {all_effects}")
    max_target = max(all_effects.keys())
    effect = all_effects[max_target]
    return effect


def explore_entire_results_history(decks, parts, language: Language, prune=None):
    failed = []
    total_lacking = 0
    failed_count = 0
    failed_cards = []
    filter_first = 50
    win = 0
    progress = tqdm(decks[:filter_first])

    # logging.getLogger().setLevel(logging.INFO)

    for my_deck in progress:
        win_message = f"Win/Fail: {win}/{failed_count}"
        progress.set_description(win_message)
        result = explore_all(language, my_deck, parts,
                             prune=prune)
        if result.has_finished():
            win += 1
        else:
            lacking = len(result.remaining_deck())
            total_lacking += lacking
            failed_count += 1
            failed.append(f"{result.remaining_deck()} - {lacking}")
            failed_cards.append(result.current_value())

    failed_cards = Counter(failed_cards)
    failed = "\n".join(failed)
    print(f"% lacking: {total_lacking / filter_first}")
    print(f"Success: {win}")
    print(f"Failed: {failed_count}")
    print(failed_cards)
    print(failed)
