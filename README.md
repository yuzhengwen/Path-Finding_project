# Number Sliding Puzzle  
---
This is a lab exercise 7 for SC1015 (Data Science and Artificial Interlligence). This exercise is create a algorithms to find the least move to solve the number sliding puzzle. 

## Introduction:
---
The problem is that we are given a grid with m number of squares and numbered blocks from 1 to n fill up the grid where n<m. Each move we are only allowed to move one move up, down, left, or right by 1 step, and only if the target square is unoccupied. The objective is to achieve a certain configuration in the least number of steps. (e.g. numeric order)

To tackle this problem, AI agents can be used to intelligently explore through the possible actions at each point in time, avoiding repetition and dead ends, and finding the shortest solution if multiple exist.

## Type of Agent:
--- 
The agent to be modeled is a **Non-Autonomous Utility-Based Agent**
>1. It is non-autonomous agent as all the information are provided and made available to agent
(built-in / pre-defined). Agent will just need to respond based on these information (number sliding 
information, initial and goal states, as well as cost) along with set of rules (search algorithm) 
provided. The agent will then figure out the best action to be taken (utility / algorithms).

>2. There may be many action sequences that can achieve the same goal. Hence, some utility 
functions need to be defined allowing the agent to reason and determine the best solution.

## Type of Environments:
  | **Properties**|   ** Elaboration**                             |
  | ------------  | ---------------------------------------------- |
  | Accessible    |                                                |
  | Deterministic |                                                |
  | Sequential    |                                                |
  | Static        |                                                |
  | Discrete      |                                                |

## Programe Formulation 
| **Properties**       | **Elaboration**                                           |
|----------------------|-----------------------------------------------------------|
| Initial State        | Randomize number:                                         |
|                      | e.g. [7, 4, 6, 8, 0, 3, 2, 1, 5]                          |
| Goal State           |      [1, 2, 3, 4, 5, 6, 7, 8, 9]                          |
| Action Sets          | Move a single block up/down/left/right to an empty space  |
| Goal Test Predicate  | Take the least steps to reach goal state                  |
| Cost Function        | Each step taken cost 1 energy from the agen               |
| Solution             | Optimal set of shifts to reach goal position from initial |
