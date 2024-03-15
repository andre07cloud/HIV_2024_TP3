from poly_sbst.common.abstract_executor import AbstractExecutor
from poly_sbst.problems.abstract_problem import AbstractProblem

class UrlTestSuiteProblem(AbstractProblem):

    def __init__(self, executor: AbstractExecutor, n_var: int = 1, n_obj=1, n_ieq_constr=0, xl=None, xu=None):
        super().__init__(executor, n_var, n_obj, n_ieq_constr, xl, xu)
        self.executor = executor
        self._name = "UrlTestsuiteProblem"
        self.previous_coverage = 0
        self.first_evaluationv = True


    def _evaluate(self, x, out, *args, **kwargs):

        tests = x[0]
        self.executor._full_coverage = []
        self.executor._coverage = set()

        for test in tests:
            #print("********TEST: ", test)
            exceptions, execution_time, coverage = self.executor._execute_input(test)
            
        fitness = len(coverage) / (len(test) + 0.1)
        self.execution_data[self.n_evals] = {"input": test, "output": fitness, "execution_time": execution_time}

        self.n_evals += 1

        out["F"] = -fitness