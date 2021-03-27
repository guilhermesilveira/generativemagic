class Checker:

    def check(self, deck):
        raise Exception("Not yet implemented")


class AreAll(Checker):
    """Checks if both of the checkers are valid"""

    def __init__(self, *all_checkers):
        self.all = all_checkers

    def check(self, deck):
        results = []
        for checker in self.all:
            result = checker.check(deck)
            if result is None:
                return None
            results.append(result)
        return results

    def __repr__(self):
        return f"AreAll({self.all})"


class AreAny(Checker):
    """Checks if any of the checkers are valid"""

    def __init__(self, *all_checkers):
        self.all = all_checkers

    def check(self, deck):
        for checker in self.all:
            result = checker.check(deck)
            if result:
                return result
        return None

    def __repr__(self):
        return f"AreAny({self.all})"
