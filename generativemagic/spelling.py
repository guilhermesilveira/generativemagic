from collections import defaultdict

from generativemagic.decks import position_to_value, position_to_suit


class Language:
    def card_name(self, c):
        pass

    def position_to_suit_name(self, k):
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


class CachedLanguage(Language):
    def __init__(self, language):
        self.language = language
        self.cards = [""]
        for c in range(1, 53):
            self.cards.append(language.card_name(c))

    def card_name(self, k):
        # print(self.cards, k)
        return self.cards[k]


class English(Language):
    def __init__(self):
        self.names = ["", "ace", "two", "three", "four", "five",
                      "six", "seven", "eight", "nine", "ten",
                      "jack", "queen", "king"]

    def card_name(self, c):
        return f"{self.names[position_to_value(c)]} of {self.position_to_suit_name(c)}"

    def position_to_suit_name(self, k):
        return ["clubs", "hearts", "spades", "diamonds"][position_to_suit(k)]


class Portuguese(Language):

    def __init__(self):
        self.names = ["", "as", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "valete",
                      "dama", "rei"]

    def card_name(self, c):
        return f"{self.names[position_to_value(c)]} de {self.position_to_suit_name(c)}"

    def position_to_suit_name(self, k):
        return ["paus", "copas", "espadas", "ouros"][position_to_suit(k)]
