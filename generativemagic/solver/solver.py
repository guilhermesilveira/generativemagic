from z3 import Solver

from generativemagic.solver.rules import Ruler
import timeit


class RuleSolver:

    def solve(self, ruler: Ruler):

        start_time = timeit.default_timer()
        solver = Solver()
        for rule in ruler.rules():
            solver.add(rule)

        print(f"Satisfiable? {solver.check()}")

        elapsed = timeit.default_timer() - start_time
        print(f"Elapsed {elapsed} seconds")
        print(solver.statistics())

        model = solver.model()
        dic_model = {}
        for d in model.decls():
            dic_model[int(model[d].__str__())] = d.name()

        print("{")
        keys = sorted(list(dic_model.keys()))
        for k in keys:
            print(f"{k}: '{dic_model[k]}',")
        print("}")
