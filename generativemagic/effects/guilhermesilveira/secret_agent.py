import numpy as np

from generativemagic.effect import Effect


class SecretAgent(Effect):
    """> Secret Agent, Guilherme Silveira
> Volunteer picks a number for the agent and does not say it (007).
> Counts the cards into a new stack. Peek the agent. Puts the stack back.
> Does a cut.
- Ends with the reverted order of the top N cards"""

    def __init__(self, codename: int):
        self._codename = codename

    def apply(self, sequence, chosen=None):
        return np.concatenate([sequence[self._codename - 1::-1],
                               sequence[self._codename:]])

    def __repr__(self):
        return f"SecretAgent({self._codename})"

    @staticmethod
    def is_ready_to_use(deck, chosen=None):
        return True
