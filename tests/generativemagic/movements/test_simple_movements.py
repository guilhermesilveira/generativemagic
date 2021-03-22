from numpy.testing import assert_array_equal

from generativemagic.movements.simple_movements import TopToBottom, BottomToTop, TopToLastToBottom, BottomToSecond


def test_top_to_bottom_move():
    deck = [1, 2, 3, 4]
    assert_array_equal(TopToBottom(1).apply(deck), [2, 3, 4, 1])
    assert_array_equal(TopToBottom(2).apply(deck), [3, 4, 1, 2])
    assert_array_equal(TopToBottom(3).apply(deck), [4, 1, 2, 3])
    assert_array_equal(TopToBottom(4).apply(deck), deck)


def test_bottom_to_top_move():
    deck = [1, 2, 3, 4]
    assert_array_equal(BottomToTop(1).apply(deck), [4, 1, 2, 3])
    assert_array_equal(BottomToTop(2).apply(deck), [3, 4, 1, 2])
    assert_array_equal(BottomToTop(3).apply(deck), [2, 3, 4, 1])
    assert_array_equal(BottomToTop(4).apply(deck), deck)


def test_top_to_last_to_bottom():
    deck = [1, 2, 3, 4]
    assert_array_equal(TopToLastToBottom().apply(deck), [2, 3, 1, 4])


def test_bottom_to_second():
    deck = [1, 2, 3, 4]
    assert_array_equal(BottomToSecond().apply(deck), [1, 4, 2, 3])
