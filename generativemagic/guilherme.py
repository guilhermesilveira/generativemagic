class Guilherme:
    """A proof of concept of an impromptu suggester for beginners to impromptu magic."""

    def __init__(self, known_effects):
        self.__known_effects = known_effects

    def suggestions_for(self, deck, chosen=None):
        return [effect for effect in self.__known_effects if effect.is_ready_to_use(deck, chosen)]
