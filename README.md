# Number Sliding Puzzle  
This is a lab exercise 8 for SC1015 (Data Science and Artificial Interlligence). We will be creating an algorithm to solve a sliding puzzle with the least moves from scratch using only built-in Python libraries

## Introduction:
The problem is that we are given a grid (mxm) with m number of squares and numbered blocks from 1 to n fill up the grid where n<(mxm).  
Each move we are only allowed to move one move up, down, left, or right by 1 step, and only if the target square is unoccupied. The objective is to achieve a certain configuration in the least number of steps. (e.g. numeric order)

To tackle this problem, we use a non-autonomous utility-based agent. The agent intelligently explores possibilities, avoiding repetition and dead ends, while making decisions on what route to explore based on a custom heuristic function.

---
# How to Use
1) Open a command prompt/terminal window in the same directory as the py file
2) Type `py main.py` and enter
3) It will ask for 3 inputs
    - Grid length: '3' represents a 3x3 grid, etc.
    - Initial position: Make sure to give the correct number of elements (denoted by grid length), separated by space. '0' represents a blank space. e.g. `1 2 3 4 0 5 6 7 8`
    - Goal position: Same as above. Use `3x3` or `4x4` to use the predefined goal positions (numeric order)
4) (Hopefully) After performing a search, it should print out the step by step solution to solve the puzzle!

---
# Solution Explanation
## Python Classes Used
### Puzzle Grid Object
Contains the puzzle grid which is a 2-d array of [m][m].
#### Key Methods
`Find Possible Swaps`: this method will locate the blank space and try to find all valid blocks surrounding it. These blocks are the only blocks able to move at the current state.  
`Swapping 2 values`: this method will find the cell position of the 2 blocks and swap their positions in the grid  
`Get Possible Positions`: A combination of the above 2 functions allow us to get a list of possible grids that can arise from a single swap at the current state.  
`Difference counter`: this is the 'h' variable in our heuristic function and calculates the number of blocks that are in a position different from the goal state.  

### Node Object
This represents a node in our tree model used to find the optimal solution.  
Each tree contains a Puzzle Grid Object, a depth counter, and a Parent Node (only the top level node aka. initial position will not have a parent)  
#### Key Methods
The most important method in a node is the `Create Children` function.  
This function uses the `GetPossiblePositions()` PuzzleGrid method and stores each possible position in a new child node with this node as parent.  
The depth counter will automatically be set as `parent.depth+1`
> The reason this object is crucial is that this way each node keeps track of its own depth. In A*/Greedy search, we may end up jumping between depth levels due to heuristic function. This way the depth is always correct.  

`Get Heuristic Function`: This is the method that will return the heuristic value of this node object. 
For A* Search: `f=g+h` where g is **depth** and h is **difference count**  

## General Functions
With all the class setup complete. There are also several important functions to be able to solve the puzzle.  

`Getting inputs`: There are some functions that help get user input to create the initial and goal grids as well as specify the grid length of the puzzle.  
`Printing path`: Another important function. Once the algorithm has found a state that satisfies the goal test predicate, the Node object will trace its parent, all the way until the initial node. Then the solution which includes every single step is printed to console.  

`SOLVE FUNCTION`: Why struggle? just use solve(puzzle) and it will be solved! (;))  
On a more serious note, with all the setup completed. The solve function is very simple.  
We only need to pass in the initial and final grid into the function.
**LOOP**:  
1) Create node based on grid
2) Do goal test predicate check (if we have reached goal position)
3) If we haven't reached goal, expand current node and add children nodes to a 'frontier' list (NOTE: We keep track of all explored states. If child node is a state we have explored, it will **not** be added  - *See below*)
4) Sort list so that node with lowest heuristic value is at the front
5) Pop first item at the front of list
6) Repeat 

## Additional Considerations
The total number of possible ways to arrange numbers 0-8 on 9 grids is 9!=362880. It is worth noting that from any given state, **not all** 362879 other states may be reachable. So the possible states may be a significantly reduced number, but nevertheless relatively large.   
Our algorithm **will not check a same state twice** for efficiency (and to prevent agent from looping back n forth between 2 states infinitely), however worst case scenarios there still may be tens of thousands of states to check through, while some setups may be inherently unsolveable!