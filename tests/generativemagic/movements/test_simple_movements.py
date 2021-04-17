from numpy.testing import assert_array_equal

from generativemagic.movements.simple_movements import TopToBottom, BottomToTop, TopToLastToBottom, BottomToSecond, \
    ReceiveToTop, ReceiveToBottom

FOUR_CARDS = [1, 2, 3, 4]


def test_top_to_bottom_move():
    assert_array_equal(TopToBottom(1).apply(FOUR_CARDS), [2, 3, 4, 1])
    assert_array_equal(TopToBottom(2).apply(FOUR_CARDS), [3, 4, 1, 2])
    assert_array_equal(TopToBottom(3).apply(FOUR_CARDS), [4, 1, 2, 3])
    assert_array_equal(TopToBottom(4).apply(FOUR_CARDS), FOUR_CARDS)


def test_bottom_to_top_move():
    assert_array_equal(BottomToTop(1).apply(FOUR_CARDS), [4, 1, 2, 3])
    assert_array_equal(BottomToTop(2).apply(FOUR_CARDS), [3, 4, 1, 2])
    assert_array_equal(BottomToTop(3).apply(FOUR_CARDS), [2, 3, 4, 1])
    assert_array_equal(BottomToTop(4).apply(FOUR_CARDS), FOUR_CARDS)


def test_top_to_last_to_bottom():
    assert_array_equal(TopToLastToBottom().apply(FOUR_CARDS), [2, 3, 1, 4])


def test_bottom_to_second():
    assert_array_equal(BottomToSecond().apply(FOUR_CARDS), [1, 4, 2, 3])


def test_receive_to_top():
    assert_array_equal(ReceiveToTop().apply(FOUR_CARDS, 5), [5, 1, 2, 3, 4])


def test_receive_to_bottom():
    assert_array_equal(ReceiveToBottom().apply(FOUR_CARDS, 5), [1, 2, 3, 4, 5])
