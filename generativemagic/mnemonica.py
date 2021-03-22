import numpy as np

MNEMONICA = np.array(['4 of clubs', '2 of hearts', '7 of diamonds', '3 of clubs',
                      '4 of hearts', '6 of diamonds', 'ace of spades', '5 of hearts',
                      '9 of spades', '2 of spades', 'queen of hearts', '3 of diamonds',
                      'queen of clubs', '8 of hearts', '6 of spades', '5 of spades',
                      '9 of hearts', 'king of clubs', '2 of diamonds', 'jack of hearts',
                      '3 of spades', '8 of spades', '6 of hearts', 'ten of clubs',
                      '5 of diamonds', 'king of diamonds', '2 of clubs', '3 of hearts',
                      '8 of diamonds', '5 of clubs', 'king of spades', 'jack of diamonds',
                      '8 of clubs', 'ten of spades', 'king of hearts', 'jack of clubs',
                      '7 of spades', 'ten of hearts', 'ace of diamonds', '4 of spades',
                      '7 of hearts', '4 of diamonds', 'ace of clubs', '9 of clubs',
                      'jack of spades', 'queen of diamonds', '7 of clubs', 'queen of spades',
                      'ten of diamonds', '6 of clubs', 'ace of hearts', '9 of diamonds']
                     )


def new_mnemonica():
    return MNEMONICA.copy()


_integer_to_mnemonica_values = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                                '7': 7, '8': 8, '9': 9, 't': 10, 'j': 11, 'q': 12, 'k': 13}


def _integer_to_mnemonica(name):
    value = _integer_to_mnemonica_values[name[0]]
    if name.endswith("clubs"):
        value += 0
    elif name.endswith("hearts"):
        value += 13
    elif name.endswith("spades"):
        value += 26
    else:
        value += 39
    return value


def mnemonica_as_integer():
    return np.array(list(map(_integer_to_mnemonica, new_mnemonica())))
