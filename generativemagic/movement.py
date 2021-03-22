import os
import pickle

from generativemagic.decks import simple_deck
from os import path


def load_movement(name):
    sequence = pickle.load(open(f"cached/movement_{name}.data", "rb"))
    return Reorder(name, sequence)


class Movement:

    def apply(self, current_stack):
        pass

    def reload(self, always_save: bool = True):
        if always_save or not path.isfile(self._get_cache_name()):
            self.save_result()
        return load_movement(self.__repr__())

    def still_can_use(self, used_so_far):
        return True

    def name(self):
        return self.__repr__()

    def save_result(self):
        result = self.apply(simple_deck() - 1)
        os.makedirs("cached", exist_ok=True)
        name = self._get_cache_name()
        pickle.dump(result, open(name, "wb"))

    def _get_cache_name(self):
        # bad looking, should not use repr..
        return f"cached/movement_{self.__repr__()}.data"


REPETITION_LIMIT = 2


class Reorder(Movement):

    def __init__(self, name, new_sequence):
        self.new_sequence = new_sequence
        self.internal_name = name
        self.simple_name = name[:name.index("(")]

    def __repr__(self):
        return f"Reorder({self.internal_name})"

    def apply(self, current_stack):
        return current_stack[self.new_sequence]

    def still_can_use(self, used_so_far):
        count = 0
        for used in used_so_far:
            if self.simple_name in used.name():
                count += 1
                if count >= REPETITION_LIMIT:
                    return False
        return True
