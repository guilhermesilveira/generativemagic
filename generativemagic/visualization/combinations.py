from typing import List, Counter

import pandas as pd
from tqdm import tqdm

from generativemagic.decks import position_to_value, deck_as_str


def all_compositions_of_fixed_length(decks: List, length: int,
                                     minimum_occurrences_per_deck: int = 1):
    compositions = Counter[str]()
    for deck in tqdm(decks):
        in_deck_occurrences = Counter[str]()
        for i in range(len(deck) - length + 1):
            card_numbers = [position_to_value(c) for c in deck[i:i + length]]
            sequence = deck_as_str(card_numbers)
            in_deck_occurrences[sequence] += 1
            if in_deck_occurrences[sequence] == minimum_occurrences_per_deck:
                compositions[sequence] += 1
    return compositions


def explore_card_combination(decks: List, lengths: List[int],
                             minimum_occurrences_per_deck: int = 1):
    results = {}
    for length in lengths:
        compositions = all_compositions_of_fixed_length(decks, length,
                                                        minimum_occurrences_per_deck=minimum_occurrences_per_deck)
        if len(compositions) == 0:
            continue
        df = pd.DataFrame.from_dict(compositions, orient='index').reset_index()
        df.columns = ["sequence", "frequency"]
        df['frequency'] /= len(decks)
        df.sort_values("frequency", ascending=False, inplace=True)
        results[length] = df
    return results
