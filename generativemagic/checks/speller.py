from collections import defaultdict

from generativemagic.spelling import Language


class IsSpelled:
    """returns a card spelled from top"""

    def __init__(self, language: Language, deltas: list):
        self._language = language
        self._deltas = deltas
        self._cached_lengths = defaultdict(set)
        for c in range(1, 53):
            name = language.card_name(c).replace(" ","")
            self._cached_lengths[len(name)].add(c)
        self.items = self._cached_lengths.keys()

    def _instructions(self, card_number, direction: str, delta: int, deal: int, mention_middle: int, len_to_find, position: int):
        # TODO discover why the int transformation is being required on numpy
        card_number = int(card_number)
        card_name = self._language.card_name(card_number)
        return card_number, direction, delta, card_name, deal, mention_middle, len_to_find, position

    def check(self, deck: list):
        # this or next card, with and without OF
        this_or_next = [0, 1]
        mention_no_middle = [0, -2, 2]
        possibilities = []

        for len_to_find in self.items:
            for delta in self._deltas:
                for mention_middle in mention_no_middle:
                    for deal in this_or_next:

                        position = len_to_find - 1 + delta + deal + mention_middle
                        card_number = deck[position]
                        if card_number in self._cached_lengths[len_to_find]:
                            instruct = self._instructions(card_number, "from top", delta, deal, mention_middle,
                                                          len_to_find, position)
                            possibilities.append(instruct)

                        position = -len_to_find - delta - deal - mention_middle
                        card_number = deck[position]
                        if card_number in self._cached_lengths[len_to_find]:
                            instruct = self._instructions(card_number, "from face", delta, deal, mention_middle,
                                                          len_to_find, position)
                            possibilities.append(instruct)

        if len(possibilities) == 0:
            return None
        return possibilities

    def __repr__(self):
        return f"IsSpelled({self._language})"
