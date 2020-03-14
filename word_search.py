import sys
from word_search_problem import WordSearchProblem
from word_search_solver import WordSearchSolver

if __name__ == "__main__":
        problem = WordSearchProblem(sys.argv[1]) if len(sys.argv) > 1 else WordSearchProblem()
        solver = WordSearchSolver(problem)
        print(solver.solve_puzzle())