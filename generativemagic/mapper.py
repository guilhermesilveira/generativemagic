from collections import defaultdict
from itertools import product

import numpy as np
import pandas as pd
from tqdm import tqdm

from generativemagic.decks import simple_deck
from generativemagic.effect import Effect


class EffectInvalidParameterError(BaseException):
    pass


def run_parameter_space(type_to_map, parameter_space, callback):
    print(parameter_space)
    items = list(product(*parameter_space))
    with tqdm(total=len(items)) as progress_bar:
        for parameters in items:
            try:
                instance: Effect = type_to_map(*parameters)
                result = instance.apply(simple_deck())
                callback(instance, result)
            except EffectInvalidParameterError:
                pass
            progress_bar.update(1)


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
    from generativemagic.effects.encyclopedia import TheMagicBreath
    from generativemagic.effects.four_aces import FourAces
    from generativemagic.effects import MathSquareMatrix
    from generativemagic.effects import ThreeMeetings
    from generativemagic.movements.faro import InFaro, OutFaro
    from generativemagic import CutAtScallop
    from generativemagic.movements.simple import TopToBottom, BottomToTop
    from generativemagic.effects.four_aces import parameter_space

    results = defaultdict(list)
    effects = [[MathSquareMatrix, [[3, 4, 5, 6], [False, True], [False, True]]],
               [ThreeMeetings, [range(10, 13), range(7, 10), [False, True]]],
               [TheMagicBreath, [range(5, 16), [False, True], [False, True]]],
               [FourAces, parameter_space()]]
    movements = [[InFaro, []],
                 [OutFaro, []],
                 [CutAtScallop, [list(range(1, 53))]],
                 [TopToBottom, [list(range(1, 27))]],
                 [BottomToTop, [list(range(1, 27))]]]
    for t, p in (effects + movements):
        map_parameter_space(t, p, append_results_to=results)
    r = [(cards, types, len(types)) for cards, types in results.items()]
    return pd.DataFrame(r, columns=["cards", "types", "amount"])
