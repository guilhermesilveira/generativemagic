from generativemagic.decks import value_and_suit_to_card, SUIT_CLUBS, SUIT_HEARTS, is_int_card
from generativemagic.effect import Effect

from generativemagic.spelling import Language, CachedLanguage, English

THREE_CLUBS = value_and_suit_to_card(3, SUIT_CLUBS)
THREE_HEARTS = value_and_suit_to_card(3, SUIT_HEARTS)
TWO_CLUBS = value_and_suit_to_card(2, SUIT_CLUBS)
REQUIRED_CARDS = [THREE_CLUBS, THREE_HEARTS, TWO_CLUBS]


class IsImpromptuSpelled:
    """returns if a SINGLE selected card can be spelled."""

    def __init__(self, can_second_deal: bool, language: Language):
        self._can_second_deal = can_second_deal
        self._language = language

    def check(self, deck, chosen=None):
        if not chosen:
            return None

        if not is_int_card(chosen):
            return None

        name = self._language.card_name(chosen)
        length = len(name.replace(" ", ""))

        # from top
        if deck[length - 1] == chosen:
            return f"Impromptu spell {name}, last letter is card"
        if deck[length] == chosen:
            return f"Impromptu spell {name}, next card is card"
        if self._can_second_deal and deck[length + 1] == chosen:
            return f"Second dealing last, impromptu spell {name}, next card is card"

        # from bottom
        if deck[-length - 1] == chosen:
            return f"Impromptu spell from bottom, {name}, next card is card"
        if deck[-length] == chosen:
            return f"Impromptu spell from bottom, {name}, last letter is card"

        return None

    def __repr__(self):
        return f"IsImpromptuSpelled({self._can_second_deal, self._language})"


class ImpromptuSpelled(Effect):

    def apply(self, sequence, chosen=None):
        pass

    def __repr__(self):
        return f"ImpromptuSpelled()"

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        return IsImpromptuSpelled(True, CachedLanguage(English())).check(deck, chosen)
