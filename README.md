# Number Sliding Puzzle  
This is a lab exercise 8 for SC1015 (Data Science and Artificial Interlligence). We will be creating an algorithm to solve a sliding puzzle with the least moves from scratch using only built-in Python libraries

## Introduction:
The problem is that we are given a grid (mxm) with m number of squares and numbered blocks from 1 to n fill up the grid where n<(mxm).  
Each move we are only allowed to move one move up, down, left, or right by 1 step, and only if the target square is unoccupied. The objective is to achieve a certain configuration in the least number of steps. (e.g. numeric order)

To tackle this problem, we use a non-autonomous utility-based agent. The agent intelligently explores possibilities, avoiding repetition and dead ends, while making decisions on what route to explore based on a custom heuristic function.

---
# How to Use
1) Open a command prompt/terminal window in the same directory as the py file
2) Type `py main.py` and enter (This will run the A* implementation, you can run the other algorithms too. Process is similar)
3) It will ask for 3 inputs
    - Grid length: '3' represents a 3x3 grid, etc.
    - Initial position: Make sure to give the correct number of elements (denoted by grid length), separated by space. '0' represents a blank space. e.g. `1 2 3 4 0 5 6 7 8`
    - Goal position: Same as above. Use `3x3` or `4x4` to use the predefined goal positions (numeric order)
4) (Hopefully) After performing a search, it should print out the step by step solution to solve the puzzle!

---
# Solution Explanation (Main: A*)
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

# Other Algorithms
After much testing, we A* seems to be the most consistent in finding the shortest path in shortest time. But 6 other algorithms have been implemented as well and are labelled accordingly.

## Algorithms that do not use a heuristic function
### Breadth First Search
BFS will search every node in each depth before expanding.   
E.g. It will expand every depth=1 node and check for goal state, if not it will expand every depth=2 node, and this repeats until goal state is found.  
This will be able to find the shortest distance to solution, but will end up expanding many unnecesary nodes and the search time gets exponentially longer.

### Depth First Search
We have 3 variations of DFS: The basic DFS, depth-limited, and iterative-deepening:  
The ***basic DFS*** is highly unsuitable for our problem and the result is completely luck based. If the first node it chooses to expand contains the goal puzzle, then it will find the solution (often not optimal), but if that node does not have the goal state, then it will forever continuously expand down one branch.
***Depth Limited*** only works if the solution is within the depth the user inputs. Even if goal state is reachable within specified depth, due to randomly exploring each branch to the end, the solution may not be optimal as well.
Lastly ***Iterative-Deepening*** will accept a max depth limit from user (can be a large number), then it will perform Depth Limited search with increasing depth limit `1 < limit < max depth limit `. It suffers from the same drawback of possibly not providing optimal solution

## Algorithms with alternate Heuristic Functions
I have also implemented 2 other algorithms that use a heuristic function similar to A*, namely ***Uniform Cost Search (UCS)*** & ***Greedy Search***.  
For UCS: `f = g(depth)`
For Greedy: `f = h(No. of blocks in the wrong position or Difference from goal)`  
Both have been proven to be less efficient than A* in finding optimal solution and searching the least amount of nodes.

# Test Cases
To observe the difference between the algorithms, we recommend working backwards from the goal state and using an initial state not more than 5 moves away from the goal state. Then you can analyse the log to see the difference in how the nodes are searched.  
As of what we have tested, the **longest** solution A* Search could find was with the initial state `0 5 2 1 3 8 6 7 4`. It takes awhile to search but the solution was an unbelievable 22 steps!! (Feel free to try solving it manually :D)  

 0 | 5 | 2 
 1 | 3 | 8 
 6 | 7 | 4 



Remember that 0 represents blank space!

(Quite often) when the search takes too long you can `ctrl+c` to stop (if running in a terminal)!