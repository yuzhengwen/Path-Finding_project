import copy

# ------------------------CLASS DEFINITIONS------------------------
class PuzzleGrid:
    def __init__(self, length):
        self.length = length
        self.grid = [[' ' for _ in range(length)] for _ in range(length)]
    def set_grid(self, grid):
        self.grid = copy.deepcopy(grid)

    def display(self):
        for row in self.grid:
            print(' | '.join(row))
            print('-' * (self.length * 4 - 1))

    def set_cell(self, row, col, value):
        if 0 <= row < self.length and 0 <= col < self.length:
            self.grid[row][col] = value
        else:
            print("Invalid row or column index")

    def get_cell(self, row, col):
        if 0 <= row < self.length and 0 <= col < self.length:
            return self.grid[row][col]
        else:
            #print("Invalid row or column index")
            return None
    def get_cell_pos(self, value):
        for i in range(self.length):
            for j in range(self.length):
                if self.grid[i][j] == value:
                    return (i, j)
        return None
    def swap_cells(self, row1, col1, row2, col2):
        temp = self.grid[row1][col1]
        self.grid[row1][col1] = self.grid[row2][col2]
        self.grid[row2][col2] = temp
    def swap_values(self, value1, value2):
        pos1 = self.get_cell_pos(value1)
        pos2 = self.get_cell_pos(value2)
        if pos1 and pos2:
            self.swap_cells(pos1[0], pos1[1], pos2[0], pos2[1])
        else:
            print("Invalid cell value")
    def clone(self):
        new_puzzle = PuzzleGrid(self.length)
        new_puzzle.set_grid(self.grid)
        return new_puzzle
    def get_diff_count(self, other):
        count = 0
        for i in range(self.length):
            for j in range(self.length):
                if self.grid[i][j] != other.grid[i][j]:
                    count += 1
        return count
    def is_equal(self, other):
        return self.get_diff_count(other) == 0
    def get_adjacent_values(self, value):
        cell_pos = self.get_cell_pos(value)
        adjacent_cells = [(cell_pos[0] + 1, cell_pos[1]), (cell_pos[0] - 1, cell_pos[1]), (cell_pos[0], cell_pos[1] + 1), (cell_pos[0], cell_pos[1] - 1)]
        adjacent_cell_values = []
        for cell in adjacent_cells:
            if self.get_cell(cell[0], cell[1]):
                adjacent_cell_values.append(self.get_cell(cell[0], cell[1]))
        return adjacent_cell_values
    def get_possible_states(self):
        possible_states = []
        adjacent_cell_values = self.get_adjacent_values('0')
        for value in adjacent_cell_values:
            new_puzzle = self.clone()
            new_puzzle.swap_values('0', value)
            possible_states.append(new_puzzle)
        return possible_states
    
class Node:
    def __init__(self, puzzle_state, parent=None):
        self.puzzle_state = puzzle_state
        self.parent = parent
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
    def get_evaluation_function(self):
        return self.depth + self.puzzle_state.get_diff_count(goal_puzzle)
    def __str__ (self):
        return f"{self.get_evaluation_function()}"
    def expand(self):
        nodes = []
        possible_states = self.puzzle_state.get_possible_states()
        for state in possible_states:
            if str(state.grid) in visited:
                continue
            nodes.append(Node(state, self))
        return nodes

# ------------------------END CLASS DEFINITIONS------------------------

default_goal4 = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '0']]
default_goal3 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]

def get_input_grid():
    inputStr = input()
    # return default goal states
    if (inputStr == "3x3"):
        return default_goal3
    if (inputStr == "4x4"):
        return default_goal4
    
    inputs = inputStr.split(' ')
    # check input has correct number of elements
    if len(inputs) != grid_length**2:
        print("Invalid grid!")
        return get_input_grid()
    # create grid from input
    grid = [[' ' for _ in range(grid_length)] for _ in range(grid_length)]
    for i in range(grid_length):
        for j in range(grid_length):
            grid[i][j] = inputs[i * grid_length + j]
    return grid

visited = set()
frontier_nodes = []
def solve(puzzle):
    frontier_nodes.append(Node(puzzle))
    
    while frontier_nodes:
        node = frontier_nodes.pop(0)
        print("")
        print("-----CURRENT NODE-----")
        print("Depth:", node.depth)
        print("evaluation_function:", node.get_evaluation_function())
        #node.puzzle_state.display()
        if node.puzzle_state.is_equal(goal_puzzle):
            print("Puzzle solved!")
            print("PATH TO SOLUTION:")
            print_path(node)
            return
        visited.add(str(node.puzzle_state.grid))
        print("-----EXPANDING NODE-----")
        children = node.expand() 
        frontier_nodes.extend(children)
        frontier_nodes.sort(key=lambda x: x.get_evaluation_function())
        #print([str(x) for x in frontier_nodes])
        print("Frontier nodes:", len(frontier_nodes))
        print("Lowest evaluation_function:", frontier_nodes[0].get_evaluation_function())
        print("Visited nodes:", len(visited))

step_count = 0
def print_path(node):
    global step_count
    if node.parent:
        print_path(node.parent)
        step_count += 1
    node.puzzle_state.display()
    print()

# ------------------------MAIN CODE------------------------
grid_length = int(input("Enter the grid length: (3 for 3x3, 4 for 4x4, etc.)"))
puzzle = PuzzleGrid(grid_length)
goal_puzzle = PuzzleGrid(grid_length)

print("Enter the initial grid:")
puzzle.set_grid(get_input_grid())
puzzle.display()

print("Enter the goal grid:")
goal_state = get_input_grid()
goal_puzzle.set_grid(goal_state)

solve(puzzle)
print("Steps:", step_count)