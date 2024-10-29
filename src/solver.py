from stack import Stack

class Solver:
    def __init__(self, maze):
        self.initial_maze = maze.copy()
        self.maze = maze.copy()
        self.start = (1, 1)
        self.visited = Stack([self.start])
        self.end = (8, 13)
        self.final_path = []
    
    def solve(self):
        # Base case - check if the stack is empty. If it is, print "No solution" and the maze
        if self.visited.is_empty():
            print("No solution")
            self.print_maze()
            return
        
        # Get the top of the stack, aka the next_move
        current = self.visited.pop()

        # Mark the current position with a "*" for self.visited
        self.maze[current[0]][current[1]] = "*"

        # Base case - check if we're at the end
        if current == self.end:
            print("Maze solved!")
            self.print_maze(current)
            self.final_path = self.visited.items.copy()
            print("Path: ", self.final_path)
            return
        
        # Get the next move. If it's not None, push the current position and the next move to the stack
        next_move = self.move(current, self.visited.peek())
        if next_move is not None:
            self.visited.push(current)
            self.visited.push(next_move)
            print("moving from", current, "to", next_move)
            return self.solve()
        
        # If we can't move, backtrack. Pass the stack and the maze to the recursive call
        print("backtracking")
        self.print_maze(current)
        return self.solve()

    def move(self, current, previous = None):
        # Get the current row and column
        row, col = current

        # Check if we can move in any direction. If we can, return the new position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            # Calculate the new position
            new_row, new_col = row + dr, col + dc

            # Check if the new position is a space and not the previous position
            if self.maze[new_row][new_col] == " " and (new_row, new_col) != previous:
                return (new_row, new_col)
        
        # If we can't move, return None. This will trigger the backtracking.
        return None
    
    def print_maze(self, current = None):
        # Print the maze. If current is not None, mark the current position with an "X"
        maze_copy = [row.copy() for row in self.maze]
        if current is not None:
            maze_copy[current[0]][current[1]] = "X"
        for row in maze_copy:
            print("".join(row))

    # this doesn't work yet
    def check_solution(self):
        solution_maze = self.initial_maze.copy()
        current = self.final_path.pop(0)
        print("Solution maze")
        for row in solution_maze:
            print("".join(row))
        if current != self.start:
            raise Exception("Path does not start at the start")
        # Check if the maze has been solved
        while not self.visited.is_empty():
            current = self.visited.pop()
            # if solution_maze[current[0]][current[1]] != " ":
            #     return False
            solution_maze[current[0]][current[1]] = "*"
            
        # print("Solution maze:\n", solution_maze)
        return current == self.end
                
    
    def __repr__(self):
        return f"Solver({self.maze})"
    