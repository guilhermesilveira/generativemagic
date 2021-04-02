from generativemagic.effect import Effect


class TwinSouls(Effect):
    """> TwinSouls, Al Baker
> Two cards are selected, two cards are revealed.
- Maintain order"""

    def apply(self, sequence, chosen=None):
        return sequence

    def __repr__(self):
        return f"TwinSouls()"

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        return True
