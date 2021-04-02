def as_number(values):
    """Receives a series of card values and returns a possible calculation as a numeric value.
    This is tricky because it must deal with non numeric cards (returning -1) and 10's in very specific
    ways."""
    all_10s = True
    for i in values:
        if i != 10:
            all_10s = False
            break
    if all_10s:
        return 10 ** len(values)

    total = 0

    for value in values:

        if value > 10:
            return -1

        total *= 10

        if value != 10:
            total += int(value)
        else:
            # value is 10, first digit is one
            if total == 0:
                total += 1
                # otherwise, ignore the 0

    return total
