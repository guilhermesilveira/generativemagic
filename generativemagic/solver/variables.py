from z3 import Int

from generativemagic.spelling import Language


def create_card_variables(language: Language):
    names = map(language.card_name, range(1, 53))
    our_vars = map(Int, names)
    return list(our_vars)
