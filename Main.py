from shutil import copyfile
from Node import Node
from SumSCBD import SumSCBD

# read and process an input file for the initial and goal states
def processFile (filename):
    f = open(filename, 'r')
    # read 4 lines and remove trailing newlines for initial and goal
    initialState = [next(f).rstrip() for line in range(4)]
    next(f) # skip blank line
    goalState = [next(f).rstrip() for line in range(4)]
    f.close()

    # turn into 2d lists
    initialState = [row.split(' ') for row in initial]
    goalState = [row.split(' ') for row in goal]

    # initial cost should be calculated
    initial = Node(initialState, None, None, None) 
    goal = SumSCBD(goalState)

    return initial, goal

def main():
    pass

main()