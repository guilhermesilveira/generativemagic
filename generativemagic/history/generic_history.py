from generativemagic.decks import KING, QUEEN
from generativemagic.history.effects_history import Effects


def grade_five_or_ten(effects: Effects, message: str, accept_king=False, accept_queen=False):
    if effects.current_value() == 5:
        effects.append(1, "Rate 5 stars " + message)
        effects.append_if(5, "Out of 5 stars ")
    elif effects.current_value() == 10:
        effects.append(1, "Rate 10 " + message)
        effects.append_if(10, "Out of 10 ")
    elif accept_king and effects.current_value() == KING:
        effects.append(1, "They are the best, the king " + message)
        effects.append_if(KING, "Of all the kings")
        effects.append_if(QUEEN, "Or queens")
    elif accept_queen and effects.current_value() == QUEEN:
        effects.append(1, "They are the best, the queen " + message)
        effects.append_if(QUEEN, "Of all the queens")
        effects.append_if(KING, "Or kings")
    else:
        return False
    return True


def almost_perfect(effects: Effects, message: str):
    if effects.current_value() == 4:
        effects.append(1, "Rate 4 stars " + message)
        effects.append_if(5, "Out of 5 stars ")
    elif effects.current_value() == 9:
        effects.append(1, "Rate 9 " + message)
        effects.append_if(10, "Out of 10 ")
    else:
        return False
    return True


def perfect_or_imperfect(effects: Effects, msg: str):
    """Checks for either a perfect or near perfect result."""
    if grade_five_or_ten(effects, msg):
        return True
    return almost_perfect(effects, msg)


def generic_101(effects: Effects, type_learning: str):
    if effects.the_next_n_values([0, 1, 2, 3]) == [1, 1, 1, 1]:
        effects.append(4, f"{type_learning} learning one on one, not in the basic sense of one on one. But mentorship")
    if effects.the_next_n_values([0, 1]) == [1, 1]:
        effects.append(2, f"{type_learning} learning one on one")


def try_all_in_any_order(conditions):
    done = [False] * len(conditions)
    changed = True
    while changed:
        changed = False
        for i, condition in enumerate(conditions):
            if not done[i]:
                if condition():
                    done[i] = True
                    changed = True
