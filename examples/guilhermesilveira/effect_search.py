import logging

from generativemagic.checks.poker import IsAcesHand
from generativemagic.checks.searchers import TypeLimiter, limit_search, Searcher, depth_limiter
from generativemagic.checks.speller import IsSpelled
from generativemagic.effects.guilhermesilveira.matrix_square import MathSquareMatrix
from generativemagic.effects.guilhermesilveira.three_meetings import ThreeMeetings
from generativemagic.mnemonica import new_mnemonica
from generativemagic.movement import load_movement
from generativemagic.movements.faro import InFaro, OutFaro
from generativemagic.movements.scallop import ScallopCut
from generativemagic.movements.simple_movements import TopToBottom, BottomToTop
from generativemagic.spelling import English


def setup_movements():
    movements = {}

    for i in [1, 2]:
        TopToBottom(i).save_result()
        movements[f"TOP_TO_BOTTOM_{i}"] = load_movement(f"TopToBottom({i})")

    movements["BOTTOM_TO_TOP_1"] = BottomToTop(1).reload()

    faro = InFaro()
    movements[faro.__repr__()] = faro.reload()

    faro = OutFaro()
    movements[faro.__repr__()] = faro.reload()

    movements["CutAtScallop_7"] = ScallopCut(7)
    movements["CutAtScallop_39"] = ScallopCut(39)
    movements["CutAtScallop_43"] = ScallopCut(43)
    movements["CutAtScallop_14"] = ScallopCut(14)
    for i in range(1, 51, 5):
        movements[f"CutAtScallop_{i}"] = ScallopCut(i)

    for i in [3, 4, 5, 6, 7]:
        movements[f'MathSquareMatrix_{i}_0'] = MathSquareMatrix(i, False, False).reload()
        # movements[f'MathSquareMatrix_{i}_1'] = MathSquareMatrix(i, True, False).reload()
        movements[f'MathSquareMatrix_{i}_2'] = MathSquareMatrix(i, False, True).reload()
        movements[f'MathSquareMatrix_{i}_3'] = MathSquareMatrix(i, True, True).reload()

    for n in range(10, 13):
        for k in range(7, 9):
            tm = ThreeMeetings(n, k, True).reload()
            movements[tm.__repr__()] = tm
            tm = ThreeMeetings(n, k, False).reload()
            movements[tm.__repr__()] = tm
    return movements


all_movements = setup_movements()

matrix_limiter = TypeLimiter().limit("MathSquareMatrix", 1).check
matrix_three_limiter = TypeLimiter().limit("MathSquareMatrix", 1).limit("ThreeMeetings", 1).check

logging.basicConfig(level=logging.INFO)

searcher = Searcher(list(all_movements.values()), matrix_limiter)
speller = IsSpelled(English(),
                    deltas=[0, -2],
                    supports_next=True)

print(searcher.search(new_mnemonica(), speller.check, depth_limiter(4)))

poker = IsAcesHand([2, 4, 5, 6], True)
print(searcher.search(new_mnemonica(), poker.check, depth_limiter(4)))

