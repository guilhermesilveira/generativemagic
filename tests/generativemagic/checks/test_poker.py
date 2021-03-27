from generativemagic.checks.poker import IsAcesHand


def test_has_aces_without_second_dealing():
    deck = [0, 1, 2, 3, 13, 1, 2, 3, 26, 1, 2, 3, 39]
    assert IsAcesHand([4], False).check(deck) == (4, [0, 4, 8, 12])


def test_has_aces_without_second_dealing_in_middle():
    deck = [1, 2, 3, 4, 0, 1, 2, 3, 13, 1, 2, 3, 26, 1, 2, 3, 39]
    assert IsAcesHand([4], False).check(deck) == (4, [4, 8, 12, 16])


def test_has_aces_without_second_dealing_with_another_hand():
    deck = [0, 1, 2, 3, 4, 13, 1, 2, 3, 4, 26, 1, 2, 3, 4, 39]
    assert IsAcesHand([4, 5], False).check(deck) == (5, [0, 5, 10, 15])


def test_has_aces_with_second_dealing():
    deck = [0, 1, 2, 3, 13, 1, 2, 3, 26, 1, 2, 3, 39]
    assert IsAcesHand([4], True).check(deck) == (4, [0, 4, 8, 12])


def test_cannot_second_deal_first_round_with_too_many_cards():
    deck = [0, 1, 2, 3, 13, 1, 2, 3, 26, 1, 2, 3, 39]
    assert not IsAcesHand([3], True).check(deck)


def test_can_second_deal_on_first_round():
    deck = [0, 1, 2, 13, 3, 1, 2, 3, 26, 1, 2, 3, 39]
    assert IsAcesHand([4], True).check(deck)


def test_can_second_deal_on_two_rounds():
    deck = [0, 1, 2, 13, 3, 1, 2, 26, 3, 1, 2, 3, 39]
    assert IsAcesHand([4], True).check(deck) == (4, [0, 0, 3])


def test_can_second_deal_on_three_rounds():
    deck = [0, 1, 2, 13, 3, 1, 2, 26, 3, 1, 2, 39]
    assert IsAcesHand([4], True).check(deck) == (4, [0, 0, 2])


def test_cannot_second_deal_a_non_ace():
    deck = [0, 1, 2, 3, 13, 1, 2, 3, 4, 26, 4, 1, 2, 3, 4, 39]
    assert not IsAcesHand([4], True).check(deck)


def test_can_second_deal_on_double_aces():
    deck = [0, 13, 1, 2, 3, 26, 1, 2, 3, 39]
    assert IsAcesHand([4], True).check(deck)


def test_can_not_second_deal_on_two_double_aces():
    deck = [0, 13, 1, 2, 3, 26, 1, 2, 39]
    assert not IsAcesHand([4], True).check(deck)


def test_can_not_second_deal_with_too_many_cards():
    deck = [0, 1, 2, 3, 4, 13, 1, 2, 3, 26, 1, 2, 3, 39]
    assert not IsAcesHand([4], True).check(deck)

    deck = [0, 1, 2, 3, 13, 1, 2, 3, 4, 26, 1, 2, 3, 39]
    assert not IsAcesHand([4], True).check(deck)

    deck = [0, 1, 2, 3, 13, 1, 2, 3, 26, 1, 2, 3, 4, 39]
    assert not IsAcesHand([4], True).check(deck)


def test_can_second_deal_on_any_missing_last_cards():
    deck = [0, 1, 2, 3, 13, 1, 2, 3, 26, 1, 2, 39]
    assert IsAcesHand([4], True).check(deck)

    deck = [0, 1, 2, 3, 13, 1, 2, 3, 26, 1, 39]
    assert IsAcesHand([4], True).check(deck)

    deck = [0, 1, 2, 3, 13, 1, 2, 3, 26, 39]
    assert IsAcesHand([4], True).check(deck)
