from generativemagic.movement import Movement

DECK_TOP = 1
DECK_BOTTOM = 52


class Effect(Movement):
    def apply(self, sequence, chosen=None):
        raise Exception(f"Effect method not yet implemented for {self}")
