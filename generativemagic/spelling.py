from collections import defaultdict

from generativemagic.decks import position_to_value, position_to_suit


def _matcher_starts(items, full_name: str):
    for i, item in enumerate(items):
        if item != "" and full_name.startswith(item):
            return i
    raise Exception(f"Did not find {full_name} in {items}")


def _matcher_ends(items, full_name: str):
    for i, item in enumerate(items):
        if full_name.endswith(item):
            return i
    raise Exception(f"Did not find {full_name} in {items}")


def _name_to_position(values, suits, name: str):
    value = _matcher_starts(values, name)
    suit = _matcher_ends(suits, name)
    return value + suit * 13


class Language:
    def card_name(self, c: int):
        pass

    def position_to_suit_name(self, k: int):
        pass

    def name_of_deck(self, deck):
        names = map(self.card_name, deck)
        return ",".join(names)

    def get_names_per_length(self):
        names = defaultdict(list)
        for c in range(1, 53):
            full_name = self.card_name(c)
            name = full_name.replace(" ", "")
            names[len(name)].append(full_name)
        return names

    def name_to_position(self, name: str):
        raise Exception(f"not implemented on {type(self)}")


class CachedLanguage(Language):
    def __init__(self, language: Language):
        self._language = language
        self.cards = [""]
        for c in range(1, 53):
            self.cards.append(language.card_name(c))

    def card_name(self, k: int):
        return self.cards[k]

    def name_to_position(self, name: str):
        return self._language.name_to_position(name)


class English(Language):
    def __init__(self):
        self._names = ["", "ace", "two", "three", "four", "five",
                       "six", "seven", "eight", "nine", "ten",
                       "jack", "queen", "king"]
        self._suits = ["clubs", "hearts", "spades", "diamonds"]

    def card_name(self, c):
        return f"{self._names[position_to_value(c)]} of {self.position_to_suit_name(c)}"

    def position_to_suit_name(self, k):
        return self._suits[position_to_suit(k)]

    def name_to_position(self, name):
        return _name_to_position(self._names, self._suits, name)


class Portuguese(Language):

    def __init__(self):
        self._names = ["", "as", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "valete",
                      "dama", "rei"]
        self._suits = ["paus", "copas", "espadas", "ouros"]

    def card_name(self, c: int):
        return f"{self._names[position_to_value(c)]} de {self.position_to_suit_name(c)}"

    def position_to_suit_name(self, k: int):
        return self._suits[position_to_suit(k)]

    def name_to_position(self, name: str):
        return _name_to_position(self._names, self._suits, name)

class Japanese(Language):
    def __init__(self):
        self._names = ["", "えーす", "に", "さん", "よん", "ご",
                       "ろく", "なな", "はち", "きゅう", "じゅう",
                       "じゃっく", "くいーん", "きんぐ"]
        self._suits = ["クラブ", "ハート", "スペード", "ダイヤ"]

    def card_name(self, c):
        return f"{self._names[position_to_value(c)]} の {self.position_to_suit_name(c)}"

    def position_to_suit_name(self, k):
        return self._suits[position_to_suit(k)]

    def name_to_position(self, name):
        return _name_to_position(self._names, self._suits, name)
