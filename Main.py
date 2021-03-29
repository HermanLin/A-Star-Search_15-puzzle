from shutil import copyfile
from PQueue import PQueue
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
    initialState = [row.split(' ') for row in initialState]
    goalState = [row.split(' ') for row in goalState]

    return initialState, goalState

def outputFile(filename, outputFileName, depth, numNodes, actions, fvalues):
    copyfile(filename, outputFileName)
    
    f = open(outputFileName, 'a')
    f.write("\n\n")
    f.write(str(depth) + "\n" + str(numNodes) + "\n")
    for action in actions:
        f.write(str(action) + " ")
    f.write("\n")
    for fvalue in fvalues:
        f.write(str(fvalue) + " ")
    f.close()


def aStar(initialState, goalState, heuristic):
    initialNode = Node(initialState, None, None, 0, heuristic)

    frontier = PQueue() # store tuples of (f(n), node)
    frontier.put((initialNode.getCost(), initialNode)) #add tuple (f(n), node) to frontier
    initStateStr = stateToString(initialNode.getState()) 
    reached = {initStateStr: initialNode.getCost()} #dict with all expanded nodes and their f(n) cost

    while not frontier.empty(): 
        currNode = frontier.get()[1]
        if currNode.getState() == goalState: # goal state has been reached
            return currNode, len(reached) # return solution node, length of reached

        # expand current node for possible moves
        children = expand(currNode, heuristic)
        for child in children:
            childState = stateToString(child.getState())

            # check if the state is already in reached
            # if it is, compare f(n) values
            if childState in reached:
                # if f(n) of the state in reached is greater than the child's f(n)
                if child.getCost() < reached[childState]:
                    reached[childState] = child.getCost()
            else: 
                reached[childState] = child.getCost()

            # add child to frontier
            frontier.put((child.getCost(), child))

    return None, 0 # solution could not be found


def stateToString(state): 
    #convert state from list to string
    tempState = [tile for row in state for tile in row]
    output = " ".join(tempState)
    return output

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
            
            action = determineAction(dx, dy) #action number
            newState = node.getState() 
            # perform swap
            newState[zX][zY], newState[sX][sY] = newState[sX][sY], newState[zX][zY]
            childNode = Node(newState, node, action, node.getDepth() + 1, heuristic)
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
    filename = ""
    
    while filename.upper() != "EXIT":
        filename = input("Enter the name of your file: ")
        outputFileName = input("Enter the name of your output file: ")
        initialState, goalState = processFile(filename)

        heuristic = SumSCBD(goalState)
        solutionNode, numNodes = aStar(initialState, goalState, heuristic)

        # fill these lists by backtracking from solutionNode -> initialNode
        actions = []
        fvalues = []
        depth = solutionNode.getDepth()

        if solutionNode: # if a solution was found
            currNode = solutionNode
            while currNode != None:
                action = currNode.getAction()
                if action != None: # disregard the initialNode's action
                    actions.insert(0, currNode.getAction())
                fvalues.insert(0, currNode.getCost())
                currNode = currNode.getParent()

        outputFile(filename, outputFileName, depth, numNodes, actions, fvalues)

main()