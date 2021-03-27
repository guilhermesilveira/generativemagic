from generativemagic.effects.truco_hand import IsTrucoHand, THREE_CLUBS, THREE_HEARTS, TWO_CLUBS


def test_has_direct_hit():
    deck = [THREE_CLUBS, THREE_HEARTS, TWO_CLUBS] + ['x'] * 49
    assert IsTrucoHand([2], False).check(deck) == (2, {'minimum distance': 3, 'position': 0, 'positions': [0, 1, 2]})


def test_has_hit_without_second_dealing():
    deck = [THREE_CLUBS, THREE_HEARTS] + ['x'] * 10 + [TWO_CLUBS] + ['x'] * 39
    assert IsTrucoHand([4], False).check(deck) == (4, {'minimum distance': 13, 'position': 0, 'positions': [0, 1, 12]})


def test_has_no_hit_without_second_dealing():
    deck = [THREE_CLUBS, THREE_HEARTS] + ['x'] * 11 + [TWO_CLUBS] + ['x'] * 38
    assert not IsTrucoHand([4], False).check(deck)


def test_has_hit_with_second_dealing():
    deck = [THREE_CLUBS, THREE_HEARTS] + ['x'] * 11 + [TWO_CLUBS] + ['x'] * 38
    assert IsTrucoHand([4], True).check(deck) == (4, {'minimum distance': 14, 'position': 0, 'positions': [0, 1, 13]})


def test_has_hit_with_second_dealing_cycled():
    deck = [THREE_CLUBS, THREE_HEARTS] + ['x'] * 38 + [TWO_CLUBS] + ['x'] * 11
    assert IsTrucoHand([4], True).check(deck) == (4, {'minimum distance': 14, 'position': 40, 'positions': [0, 1, 40]})
