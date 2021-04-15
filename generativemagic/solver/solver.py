import logging

from z3 import Solver

from generativemagic.solver.rules import Ruler
import timeit


class RuleSolver:

    def solve(self, ruler: Ruler):

        start_time = timeit.default_timer()
        solver = self._create_solver(ruler)

        print(f"Satisfiable? {solver.check()}")

        elapsed = timeit.default_timer() - start_time
        print(f"Elapsed {elapsed} seconds")
        print(solver.statistics())

        model = solver.model()
        if model:
            self._print_result(model)
        else:
            print("No model was found")

    def _print_result(self, model):
        dic_model = {}
        for d in model.decls():
            dic_model[int(model[d].__str__())] = d.name()
        print("{")
        keys = sorted(list(dic_model.keys()))
        for k in keys:
            print(f"{k}: '{dic_model[k]}',")
        print("}")

    def _create_solver(self, ruler):
        solver = Solver()
        unique_rules = set(ruler.rules())
        logging.info(f"Using {len(unique_rules)} unique constraints")
        for rule in unique_rules:
            solver.add(rule)
        return solver
