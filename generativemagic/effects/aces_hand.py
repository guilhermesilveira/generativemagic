from generativemagic.checks.poker import IsAcesHand
from generativemagic.effect import Effect


class AcesHand(Effect):

    def apply(self, sequence):
        result = IsAcesHand([4, 5], True).get_first_ace(sequence)
        raise Exception(f"To be implemented at {result}")

    def __repr__(self):
        return f"AcesHand()"

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        return IsAcesHand([4, 5], True).check(deck)
