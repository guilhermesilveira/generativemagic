def np_index(items, x):
    """Where is x in ar? This is a linear search.

    Parameters:
       items: numpy array to search for
       x: item to be found

    Returns:
       the position or -1 if not found"""

    for i in range(len(items)):
        if items[i] == x:
            return i
    return -1


def flat_map(xs):
    """Surprisingly computational efficient implementation for a flat map"""
    mapped = []
    for x in xs:
        mapped.extend(x)
    return mapped


def cards_positions(deck, cards):
    """Returns the card positions for all cards requested"""
    positions = [np_index(deck, card) for card in cards]
    return sorted(positions)
