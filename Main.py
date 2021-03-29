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
    initialNode = Node(initial, None, None, heuristic)

    frontier = PriorityQueue() # store tuples of (f(n), node)
    frontier.put((initialNode.getCost(), initialNode))
    reached = {initialState : initialNode.getCost()}

    while not frontier.empty():
        currNode = frontier.get()
        if currNode.getCost() == 0: # a cost of 0 means goal node
            return currNode

    return None # solution could not be found


def expand(node, heuristic):
    # expand a node for possible moves
    # return a list of possible moves as nodes

    children = []
    zX, zY = node.getValuePos(0)
    # loop through possible swaps according to 0's position
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            sX, sY = zX + dx, zY + dy
            if dx == 0 and dy == 0:
                continue # the potential move creates the same state, skip
            if sX < 0 or sX > 3 or sY < 0 or sY > 3:
                continue # the potential move is out of bounds, skip
            
            action = determineAction(dx, dy)
            newState = node.getState()
            # perform swap
            newState[zX][zY], newState[sX][sY] = newState[sX][sY], newState[zX][zY]
            childNode = Node(newState, node, action, heuristic)
            children.append(childNode)

    return children


def determineAction(dx, dy):
    if dy == -1 and dx == 0: return 1     # left
    if dy == -1 and dx == -1: return 2    # up-left
    if dy == 0 and dx == -1: return 3     # up
    if dy == 1 and dx == -1: return 4     # up-right
    if dy == 1 and dx == 0: return 5      # right
    if dy == 1 and dx == 1: return 6      # down-right
    if dy == 0 and dx == 1: return 7      # down
    if dy == -1 and dx == 1: return 8     # down-left

def main():
    # test stuff
    testState = [[1,2,3,4],[5,0,6,7],[8,9,10,11],[12,13,14,15]]
    smallState = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,13,14,15]]
    goalState = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

    heuristic = SumSCBD(goalState)
    testNode = Node(testState, None, None, heuristic)
    smallNode = Node(smallState, None, None, heuristic)

    '''
    print("testNode:", testNode._state, testNode._parent, testNode._action, testNode.getCost())
    children = expand(testNode, heuristic)
    print("expanding testNode, number of children:", len(children))
    for child in children:
        print(child.getState())
    '''

    print("smallNode:", smallNode._state, smallNode._parent, smallNode._action, smallNode.getCost())
    moreChildren = expand(smallNode, heuristic)
    print("smallNode addr:", smallNode)
    print("expanding smallNode, number of children:", len(moreChildren))
    for child in moreChildren:
        print(child.getState())
        print(child._parent, child._action, child.getCost())
        print()

main()