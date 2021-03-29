from shutil import copyfile
from queue import PriorityQueue
from Node import Node
from SumSCBD import SumSCBD


def processFile (filename):
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

def aStar (initalState, heuristic):
    initialNode = Node(initial, None, None, None)
    initialNode._cost = heuristic(initialNode)

    frontier = PriorityQueue() # store tuples of (f(n), node)
    frontier.put((initialNode.getCost(), initialNode))
    reached = {initialState : initialNode.getCost()}

    while not frontier.empty():
        pass

def main():
    pass

main()