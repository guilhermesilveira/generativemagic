from generativemagic.effects.impromptu_revelation import *

from generativemagic.spelling import CachedLanguage, English

english = CachedLanguage(English())


def test_has_direct_hit_from_top():
    deck = ['x'] * 11 + [THREE_CLUBS] + ['x'] * 40
    assert IsImpromptuSpelled(False, english).check(deck,
                                                    THREE_CLUBS) == "Impromptu spell three of clubs, last letter is card"


def test_has_next_hit_from_top():
    deck = ['x'] * 12 + [THREE_CLUBS] + ['x'] * 39
    assert IsImpromptuSpelled(False, english).check(deck,
                                                    THREE_CLUBS) == "Impromptu spell three of clubs, next card is card"


def test_has_next_hit_with_second_deal_from_top():
    deck = ['x'] * 13 + [THREE_CLUBS] + ['x'] * 38
    assert IsImpromptuSpelled(True, english).check(deck,
                                                   THREE_CLUBS) == "Second dealing last, impromptu spell three of clubs, next card is card"


def test_has_direct_hit_from_bottom():
    deck = ['x'] * 40 + [THREE_CLUBS] + ['x'] * 11
    assert IsImpromptuSpelled(False, english).check(deck,
                                                    THREE_CLUBS) == "Impromptu spell from bottom, three of clubs, last letter is card"


def test_has_next_hit_from_bottom():
    deck = ['x'] * 39 + [THREE_CLUBS] + ['x'] * 12
    assert IsImpromptuSpelled(False, english).check(deck,
                                                    THREE_CLUBS) == "Impromptu spell from bottom, three of clubs, next card is card"
