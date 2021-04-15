from collections import defaultdict
from functools import partial
from itertools import product
from multiprocessing import Pool
from typing import List, Type

import numpy as np
import pandas as pd
from tqdm import tqdm

from generativemagic.decks import simple_deck
from generativemagic.effect import Effect


class EffectInvalidParameterError(BaseException):
    pass


def explore_single(parameters, type_to_map: Type, deck_creator):
    try:
        instance: Effect = type_to_map(*parameters)
        result = instance.apply(deck_creator())
        return instance, result
    except EffectInvalidParameterError:
        return None


def run_parameter_space(type_to_map: Type, parameter_space, callback=None, deck_creator=simple_deck, threads=1):
    items = [item for item in product(*parameter_space)]
    results = []

    p = partial(explore_single, type_to_map=type_to_map, deck_creator=deck_creator)

    with Pool(threads) as pool:
        progress = tqdm(pool.imap(p, items), total=len(items))
        for pair in progress:
            if not pair:
                continue
            instance, result = pair
            if callback:
                callback(instance, result)
            results.append(result)
    return results


def collect_parameter_space(type_to_map, parameter_space):
    results = set()

    def appender(_, result):
        results.add(np.array2string(result, max_line_width=10000))

    run_parameter_space(type_to_map, parameter_space, appender)
    return results


def map_parameter_space(type_to_map, parameter_space, append_results_to=None):
    if append_results_to:
        results = append_results_to
    else:
        results = defaultdict(list)

    def appender(instance, result):
        results[np.array2string(result, max_line_width=10000)].append(instance.__repr__())

    run_parameter_space(type_to_map, parameter_space, appender)
    return results


def catalog_parameter_space():
    results = defaultdict(list)
    from generativemagic.effects.four_aces import parameter_space
    from generativemagic.effects.four_aces import FourAces
    from generativemagic.effects.guilhermesilveira.matrix_square import MathSquareMatrix
    from generativemagic.effects.hugard_encyclopedia.encyclopedia import TheMagicBreath
    from generativemagic.movements.simple_movements import TopToBottom
    from generativemagic.movements.simple_movements import BottomToTop

    effects = [[MathSquareMatrix, [[3, 4, 5, 6], [False, True], [False, True]]],
               # [ThreeMeetings, [range(10, 13), range(7, 10), [False, True]]],
               [TheMagicBreath, [range(5, 16), [False, True], [False, True]]],
               [FourAces, parameter_space()]]
    movements = [
        # [InFaro, []],
        #          [OutFaro, []],
        #          [CutAtScallop, [list(range(1, 53))]],
        [TopToBottom, [list(range(1, 27))]],
        [BottomToTop, [list(range(1, 27))]]]
    for t, p in (effects + movements):
        map_parameter_space(t, p, append_results_to=results)
    r = [(cards, types, len(types)) for cards, types in results.items()]
    return pd.DataFrame(r, columns=["cards", "types", "amount"])
