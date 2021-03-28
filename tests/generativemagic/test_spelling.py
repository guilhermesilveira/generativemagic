import pytest

from generativemagic.spelling import _matcher_starts, _matcher_ends, _name_to_position, English

SUITS = ["clubs", "hearts", "spades", "diamonds"]
VALUES = ["", "ace", "two", "three", "four", "five"]


def test_matcher_ends():
    assert _matcher_ends(SUITS, "aces of hearts") == 1
    assert _matcher_ends(SUITS, "aces of spades") == 2


def test_matcher_ends_does_not_find():
    with pytest.raises(Exception, match=r"Did not find aces of brazilians.*"):
        _matcher_ends(SUITS, "aces of brazilians")


def test_matcher_starts():
    assert _matcher_starts(SUITS, "hearts of aces") == 1
    assert _matcher_starts(SUITS, "spades of aces") == 2


def test_matcher_starts_does_not_find():
    with pytest.raises(Exception, match=r"Did not find brazilians of aces.*"):
        _matcher_starts(SUITS, "brazilians of aces")


def test_name_to_position():
    assert _name_to_position(VALUES, SUITS, "ace of clubs") == 1
    assert _name_to_position(VALUES, SUITS, "two of clubs") == 2
    assert _name_to_position(VALUES, SUITS, "ace of hearts") == 14
    assert _name_to_position(VALUES, SUITS, "ace of spades") == 27
    assert _name_to_position(VALUES, SUITS, "ace of diamonds") == 40


def test_matcher_starts_does_not_find():
    with pytest.raises(Exception, match=r"Did not find ace of brazilians.*"):
        _name_to_position(SUITS, VALUES, "ace of brazilians")


def test_english_name_to_position():
    assert English().name_to_position("ace of clubs") == 1
    assert English().name_to_position("two of clubs") == 2
    assert English().name_to_position("ace of hearts") == 14
    assert English().name_to_position("ace of spades") == 27
    assert English().name_to_position("ace of diamonds") == 40
