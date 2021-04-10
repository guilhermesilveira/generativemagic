from generativemagic.decks import SUIT_CLUBS, value_and_suit_to_card, position_to_suit, SUIT_DIAMONDS, SUIT_SPADES, \
    SUIT_HEARTS, position_to_value, deck_as_str


def test_position_to_suit():
    for i in range(13 * 0 + 1, 13 * 1 + 1):
        assert position_to_suit(i) == SUIT_CLUBS
    for i in range(13 * 1 + 1, 13 * 2 + 1):
        assert position_to_suit(i) == SUIT_HEARTS
    for i in range(13 * 2 + 1, 13 * 3 + 1):
        assert position_to_suit(i) == SUIT_SPADES
    for i in range(13 * 3 + 1, 13 * 4 + 1):
        assert position_to_suit(i) == SUIT_DIAMONDS


def test_position_to_value():
    for i in range(1, 13 + 1):
        assert position_to_value(SUIT_CLUBS * 13 + i) == i
    for i in range(1, 13 + 1):
        assert position_to_value(SUIT_HEARTS * 13 + i) == i
    for i in range(1, 13 + 1):
        assert position_to_value(SUIT_SPADES * 13 + i) == i
    for i in range(1, 13 + 1):
        assert position_to_value(SUIT_DIAMONDS * 13 + i) == i


def test_value_and_suit_to_card():
    for i in range(1, 13 + 1):
        assert value_and_suit_to_card(i, SUIT_CLUBS) == SUIT_CLUBS * 13 + i
    for i in range(1, 13 + 1):
        assert value_and_suit_to_card(i, SUIT_HEARTS) == SUIT_HEARTS * 13 + i
    for i in range(1, 13 + 1):
        assert value_and_suit_to_card(i, SUIT_SPADES) == SUIT_SPADES * 13 + i
    for i in range(1, 13 + 1):
        assert value_and_suit_to_card(i, SUIT_DIAMONDS) == SUIT_DIAMONDS * 13 + i


def test_deck_as_str():
    assert "1,3,2,4" == deck_as_str([1, 3, 2, 4])
    assert "" == deck_as_str([])
