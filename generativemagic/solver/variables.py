from z3 import Int

from generativemagic.spelling import Language


def create_card_variables(language: Language):
    names = language.all_names()
    our_vars = map(Int, names)
    return list(our_vars), names
