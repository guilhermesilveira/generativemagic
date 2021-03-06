import importlib
from collections import defaultdict
from typing import Tuple, List

from generativemagic.decks import position_to_value, position_to_suit


def _matcher_starts(items, full_name: str) -> int:
    for i, item in enumerate(items):
        if item != "" and full_name.startswith(item):
            return i
    raise Exception(f"Did not find {full_name} in {items}")


def _matcher_ends(items, full_name: str) -> int:
    for i, item in enumerate(items):
        if full_name.endswith(item):
            return i
    raise Exception(f"Did not find {full_name} in {items}")


def _name_to_position(values: Tuple, suits: Tuple, name: str) -> int:
    value = _matcher_starts(values, name)
    suit = _matcher_ends(suits, name)
    return value + suit * 13


class Language:
    """Default structure for a basic language implementation in generative magic."""

    def card_name(self, c: int) -> str:
        raise Exception(f"not implemented on {type(self)}")

    def position_to_suit_name(self, k: int) -> str:
        raise Exception(f"not implemented on {type(self)}")

    def name_to_position(self, name: str) -> int:
        raise Exception(f"not implemented on {type(self)}")

    def name_of_deck(self, deck: List[int]) -> str:
        names = map(self.card_name, deck)
        return ",".join(names)

    def get_names_per_length(self):
        names = defaultdict(list)
        for c in range(1, 53):
            full_name = self.card_name(c)
            name = full_name.replace(" ", "")
            names[len(name)].append(full_name)
        return names

    def all_names(self) -> List[str]:
        return list(map(self.card_name, range(1, 53)))


class CachedLanguage(Language):
    """Implementation that caches all card names."""

    def __init__(self, language: Language):
        self._language = language
        self._cards = [""]
        for c in range(1, 53):
            self._cards.append(language.card_name(c))

    def card_name(self, k: int):
        return self._cards[k]

    def name_to_position(self, name: str):
        return self._language.name_to_position(name)

    def position_to_suit_name(self, k: int):
        return self._language.position_to_suit_name(k)


class SimpleLanguage(Language):
    """A base implementation for most languages. It should be enough for several languages."""

    def __init__(self, names: Tuple, suits: Tuple):
        self._names = names
        self._suits = suits

    def position_to_suit_name(self, k):
        return self._suits[position_to_suit(k)]

    def name_to_position(self, name):
        return _name_to_position(self._names, self._suits, name)

    def card_name(self, c):
        return self.connect_value_and_suit(self._names[position_to_value(c)],
                                           self.position_to_suit_name(c))

    def connect_value_and_suit(self, value, suit):
        raise Exception(f"Not yet implemented for {self}")


class English(SimpleLanguage):
    def __init__(self):
        super().__init__(("", "ace", "two", "three", "four", "five",
                          "six", "seven", "eight", "nine", "ten",
                          "jack", "queen", "king"),
                         ("clubs", "hearts", "spades", "diamonds"))

    def connect_value_and_suit(self, value, suit):
        return f"{value} of {suit}"


class PortugueseCommon(SimpleLanguage):

    def __init__(self):
        super().__init__(("", "as", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
                          "valete", "dama", "rei"),
                         ("paus", "cora????o", "espadas", "diamantes"))

    def connect_value_and_suit(self, value, suit):
        return f"{value} de {suit}"


class Portuguese(SimpleLanguage):

    def __init__(self):
        super().__init__(("", "as", "dois", "tres", "quatro", "cinco",
                          "seis", "sete", "oito", "nove", "dez",
                          "valete", "dama", "rei"),
                         ("paus", "copas", "espadas", "ouros"))

    def connect_value_and_suit(self, value, suit):
        return f"{value} de {suit}"


class French(SimpleLanguage):

    def __init__(self):
        super().__init__(("", "as", "deux", "trois", "quatre", "cinq",
                          "six", "sept", "huit", "neuf", "dix",
                          "valet", "dame", "roi"),
                         ("tr??fles", "c??urs", "piques", "carreaux"))

    def connect_value_and_suit(self, value, suit):
        return f"{value} de {suit}"


class Spanish(SimpleLanguage):

    def __init__(self):
        super().__init__(("", "as", "dos", "tres", "cuatro", "cinco",
                          "seis", "siete", "ocho", "nueve", "diez",
                          "jota", "reina", "rei"),
                         ("tr??boles", "corazones", "picas", "diamantes"))

    def connect_value_and_suit(self, value, suit):
        return f"{value} de {suit}"


class Japanese(SimpleLanguage):
    def __init__(self):
        super().__init__(("", "?????????", "???", "??????", "??????", "???",
                          "??????", "??????", "??????", "?????????", "?????????",
                          "????????????", "????????????", "?????????"),
                         ("?????????", "?????????", "????????????", "?????????"))

    def connect_value_and_suit(self, value, suit):
        return f"{suit}???{value}"


class Translator:
    """Translates from one language into another."""

    def __init__(self, original: Language, target: Language):
        self._original = original
        self._target = target

    def translate(self, name: str):
        position = self._original.name_to_position(name)
        return self._target.card_name(position)

    def revert(self):
        return Translator(self._target, self._original)


def instantiate_language(name: str) -> Language:
    """Instantiates a cached version of a language based on its name"""
    module = importlib.import_module("generativemagic.spelling")
    class_ = getattr(module, name)
    language = CachedLanguage(class_())
    return language
