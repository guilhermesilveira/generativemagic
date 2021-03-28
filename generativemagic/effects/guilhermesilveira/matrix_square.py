from generativemagic.deck_operations import stack_into, concatenate, revert
from generativemagic.effect import Effect


class MathSquareMatrix(Effect):
    """The famous two matrix math magic. But with a few twists that allows better control of the deck."""

    def __init__(self, n: int, turn_after_first_split: bool = True, first_in_same_stack: bool = False,
                 deal_from_top=True, back_to_top=True):
        self.__back_to_top = back_to_top
        self.__n = n
        self.__turn_after_first_split = turn_after_first_split
        self.__first_in_same_stack = first_in_same_stack
        self.__deal_from_top = deal_from_top

    def apply(self, sequence):
        if not self.__deal_from_top:
            sequence = revert(sequence)

        stacks, remaining = stack_into(self.__n, self.__n, sequence, same_stack=self.__first_in_same_stack)
        stacks = concatenate(stacks)
        # fake shuffle
        if not self.__turn_after_first_split:
            stacks = revert(stacks)
        stacks, _ = stack_into(self.__n, self.__n, stacks)
        stacks = concatenate(stacks)

        if self.__back_to_top:
            remaining = revert(remaining)

        joined = concatenate([stacks, remaining])

        if not self.__deal_from_top and self.__back_to_top:
            joined = revert(joined)

        return joined

    def __repr__(self):
        return f"MathSquareMatrix({self.__n},turn_after_first_split={self.__turn_after_first_split},first_in_same_stack={self.__first_in_same_stack},deal_from_top={self.__deal_from_top},back_to_top={self.__back_to_top})"
