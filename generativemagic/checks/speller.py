from collections import defaultdict

from generativemagic.spelling import Language


class IsSpelled:
    """returns a card spelled from top"""

    def __init__(self, language: Language, deltas):
        self._language = language
        self._deltas = deltas
        self._cached_lengths = defaultdict(set)
        for c in range(1, 53):
            name = language.card_name(c)
            self._cached_lengths[len(name)].add(c)
        self.items = self._cached_lengths.keys()

    def check(self, deck):
        # this or next card, with and without OF
        this_or_next = [0, 1, -2, -1]
        possibilities = []
        for len_to_find in self.items:
            for delta in self._deltas:
                for deal in this_or_next:
                    c = deck[len_to_find - 1 + delta + deal]
                    if c in self._cached_lengths[len_to_find]:
                        # TODO discover why the int transformation is being required on numpy
                        possibilities.append((c, len_to_find, delta, self._language.card_name(int(c))))
                    c = deck[-len_to_find + delta - deal]
                    if c in self._cached_lengths[len_to_find]:
                    #     TODO discover why the int transformation is being required on numpy
                        possibilities.append((c, len_to_find, delta, self._language.card_name(int(c))))
        if len(possibilities) == 0:
            return None
        return possibilities

    def __repr__(self):
        return f"IsSpelled({self._language})"
