from generativemagic.decks import simple_deck, value_and_suit_to_card, SUIT_DIAMONDS
from generativemagic.effects.aces_hand import AcesHand
from generativemagic.effects.four_aces import FourAces
from generativemagic.effects.guilhermesilveira.matrix_square import MathSquareMatrix
from generativemagic.effects.hugard_encyclopedia.encyclopedia import PhenomenalThoughtCardsRuler
from generativemagic.effects.hugard_encyclopedia.simplified_reverse import SimplifiedReverse
from generativemagic.effects.hugard_encyclopedia.thought_transference import ThoughtTransference
from generativemagic.effects.impromptu_revelation import ImpromptuSpelled

from generativemagic.effects.truco_hand import TrucoHand
from generativemagic.guilherme import Guilherme

# This is an example on how to use generative magic to suggest
# effects impromptu. Feed in the current sequence of effects you have done
# and you get out a list of possible impromptu effects to do next.

deck = simple_deck()  # Starts with a simple deck in Ace to King order

# Executes a simple math square matrix effect, from start to end
deck = MathSquareMatrix(3, False, False).apply(deck)
chosen = value_and_suit_to_card(7, SUIT_DIAMONDS)

# Ask for basic suggestions
suggestions = Guilherme([FourAces,
                         PhenomenalThoughtCardsRuler,
                         AcesHand,
                         TrucoHand,
                         ImpromptuSpelled,
                         SimplifiedReverse,
                         ThoughtTransference]).suggestions_for(deck, chosen)

# Prints the suggestions
print(f"Found a total of {len(suggestions)} suggestions")
for suggestion in suggestions:
    setup = suggestion.is_ready_to_use(deck, chosen=chosen)
    print(f"For {suggestion} use setup and get result {setup}")

# Next steps:
# Instead of using Guilherme the impromptu suggester, you can use a searcher to determine
# the order of the math square matrix reordering steps if you knew your next step, or if
# you want to have more options as suggestions.
