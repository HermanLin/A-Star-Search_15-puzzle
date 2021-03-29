from shutil import copyfile
from queue import PriorityQueue
from Node import Node
from SumSCBD import SumSCBD


def processFile(filename):
    # read and process an input file for the initial and goal states

    f = open(filename, 'r')
    # read 4 lines and remove trailing newlines for initial and goal
    initialState = [next(f).rstrip() for line in range(4)]
    next(f) # skip blank line
    goalState = [next(f).rstrip() for line in range(4)]
    f.close()

    # turn into 2d lists
    initialState = [row.split(' ') for row in initial]
    goalState = [row.split(' ') for row in goal]

    return initialState, goalState


def aStar(initalState, heuristic):
    initialNode = Node(initial, None, None, None)
    initialNode._cost = heuristic(initialNode)

    frontier = PriorityQueue() # store tuples of (f(n), node)
    frontier.put((initialNode.getCost(), initialNode))
    reached = {initialState : initialNode.getCost()}

    while not frontier.empty():
        currNode = frontier.get()
        if currNode.getCost() == 0: # a cost of 0 means goal node
            return currNode


def expand(node):
    # expand a node for possible moves
    # return a list of possible moves as nodes

    children = []
    currState = node.getState()
    zeroX, zeroY = node.getValuePos(0)
    # loop through possible swaps according to 0's position
    for i in range(-1, 2):
        for j in range(-1, 2):
            pass

def determineAction(i, j):
    if i == -1 and j == 0: return 1     # left
    if i == -1 and j == -1: return 2    # up-left
    if i == 0 and j == -1: return 3     # up
    if i == 1 and j == -1: return 4     # up-right
    if i == 1 and j == 0: return 5      # right
    if i == 1 and j == 1: return 6      # down-right
    if i == 0 and j == 1: return 7      # down
    if i == -1 and j == 1: return 8     # down-left

def main()):
    pass

main()