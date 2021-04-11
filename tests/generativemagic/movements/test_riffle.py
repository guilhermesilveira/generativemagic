from numpy.testing import assert_array_equal

from generativemagic.decks import simple_deck
from generativemagic.movements.riffle import riffle_generator, RiffleShuffle
from generativemagic.movements.simple_movements import TopToBottom, BottomToTop, TopToLastToBottom, BottomToSecond


def test_all_simple_riffles():
    assert list(riffle_generator(0)) == []
    assert list(riffle_generator(1)) == [[0, 1], [1]]
    assert list(riffle_generator(2)) == [[0, 1, 1], [0, 2], [1, 1], [2]]
    assert list(riffle_generator(3)) == [[0, 1, 1, 1], [0, 1, 2], [0, 2, 1], [0, 3], [1, 1, 1], [1, 2], [2, 1], [3]]
    assert len(list(riffle_generator(4))) == 2 ** 4
    assert len(list(riffle_generator(15))) == 2 ** 15


def test_full_riffle():
    assert_array_equal(RiffleShuffle([0, 3, 2, 1]).apply(simple_deck()), \
                       [27, 28, 29, 1, 2, 30] + list(range(3, 27)) + list(range(31, 53)))
