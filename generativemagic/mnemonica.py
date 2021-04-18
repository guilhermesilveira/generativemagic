import numpy as np

from generativemagic.spelling import English

MNEMONICA_AS_STRING = np.array(['four of clubs', 'two of hearts', 'seven of diamonds', 'three of clubs',
                                'four of hearts', 'six of diamonds', 'ace of spades', 'five of hearts',
                                'nine of spades', 'two of spades', 'queen of hearts', 'three of diamonds',
                                'queen of clubs', 'eight of hearts', 'six of spades', 'five of spades',
                                'nine of hearts', 'king of clubs', 'two of diamonds', 'jack of hearts',
                                'three of spades', 'eight of spades', 'six of hearts', 'ten of clubs',
                                'five of diamonds', 'king of diamonds', 'two of clubs', 'three of hearts',
                                'eight of diamonds', 'five of clubs', 'king of spades', 'jack of diamonds',
                                'eight of clubs', 'ten of spades', 'king of hearts', 'jack of clubs',
                                'seven of spades', 'ten of hearts', 'ace of diamonds', 'four of spades',
                                'seven of hearts', 'four of diamonds', 'ace of clubs', 'nine of clubs',
                                'jack of spades', 'queen of diamonds', 'seven of clubs', 'queen of spades',
                                'ten of diamonds', 'six of clubs', 'ace of hearts', 'nine of diamonds']
                               )

MNEMONICA_AS_INTEGER = np.array(list(map(English().name_to_position, MNEMONICA_AS_STRING)))


def new_mnemonica_as_string():
    return MNEMONICA_AS_STRING.copy()


def new_mnemonica():
    return MNEMONICA_AS_INTEGER.copy()
