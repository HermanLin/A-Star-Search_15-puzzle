# A-Star-Search_15-Puzzle

**Project Description:** Implement the _A* Search Algorithm with Graph Search_ for solving the 15-
puzzle problem as described below. Use sum of chessboard distances of tiles from their goal
positions as heuristic function, where chessboard distance is defined as the maximum of the
horizontal and vertical distances. 

**15-Puzzle Problem:** On a 4 x 4 board there are 15 tiles numbered from 1 to 15 and a blank
position. A tile can slide into the blank position if it is horizontally, vertically or diagonally
adjacent to the blank position. Given a start board configuration and a goal board configuration,
find a sequence of moves to reach the goal configuration from the start configuration. The goal is
to find a solution with minimum number of moves. 
To solve the puzzle problem, we define eight virtual moves for the blank position:
1. Left
2. Up-left
3. Up
4. Up-right
5. Right
6. Down-right
7. Down
8. Down-left

**Input and Output File Format:** 

The program will read in the initial and goal states from a text file that contains nine lines as shown:
```
n n n n
n n n n
n n n n 
n n n n

m m m m
m m m m
m m m m
m m m m
```

Lines 1 to 4 contain the tile pattern for the initial state and lines 6 to 9 contain the tile pattern for the goal state. Line 5 is a blank line. _n_ and _m_ are integers that range from 0 to 15. Integer 0 represents a blank position and integers 1 to 15 represent the tile numbers. Note: puzzles submitted are assumed to be solvable up to the goal state.

The program will produce an output text file that contains 14 lines as shown below:
```
n n n n
n n n n
n n n n 
n n n n

m m m m
m m m m
m m m m
m m m m

d
N
A A A A A A A . . .
f f f f f f f . . .
```
Lines 1 to 9 contain the tile patterns as shown in the input text file. Line 10 is a blank line. Line 11 is the depth level _d_ of the shallowest goal node found by the _A* Search Algorithm_ (assume the root node is at level 0). Line 12 is the total number of nodes _N_ generated in the tree (including the root node). Line 13 contains the solution that was found which will be displayed as a sequence of actions (from root node to goal node) represented by the _A's_. Each _A_ is a digit from 1 to 8 representing a virtual move of the blank position as indicated by the moves listed above. Line 14 contains the _f(n)_ values of the nodes along the solution path, from root node to the goal node. There should be _d_ number of A values in Line 13 and _d_+1 number of _f_ values in Line 14.
