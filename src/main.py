from maze import gen_maze
from solver import Solver

def main():
    maze = gen_maze()
    solver = Solver(maze)
    solver.solve()
    print(solver.check_solution())

main()