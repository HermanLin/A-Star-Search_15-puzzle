from shutil import copyfile
from AStar import AStar


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

def main():
    filename = ""
    
    while True:
        filename = input("Enter the name of your file: ")
        if filename.upper() == "EXIT":
            break
        outputFileName = input("Enter the name of your output file: ")
        initialState, goalState = processFile(filename)

        aStarSearch = AStar(initialState, goalState)

        solutionNode, numNodes = aStarSearch.aStar()

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