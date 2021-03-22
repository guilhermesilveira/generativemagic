import numpy as np


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
