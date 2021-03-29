from shutil import copyfile
from Node import Node

# read and process an input file for the initial and goal states
def processFile (filename):
    f = open(filename, 'r')
    # read 4 lines and remove trailing newlines for initial and goal
    initial = [next(f).rstrip() for line in range(4)]
    next(f) # skip blank line
    goal = [next(f).rstrip() for line in range(4)]
    f.close()

    # turn into 2d lists
    initial = [row.split(' ') for row in initial]
    goal = [row.split(' ') for row in goal]

    return initial, goal

def main():
    pass

main()