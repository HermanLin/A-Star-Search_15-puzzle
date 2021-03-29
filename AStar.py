from PQueue import PQueue
from Node import Node
from SumSCBD import SumSCBD

class AStar:

    def __init__(self, iState, gState):
        self._initialState = iState
        self._goalState = gState
        self._heuristic = SumSCBD(gState)

    def aStar(self):
        initialNode = Node(self._initialState, None, None, 0, self._heuristic)

        frontier = PQueue() # store tuples of (f(n), node)
        frontier.put((initialNode.getCost(), initialNode)) #add tuple (f(n), node) to frontier
        initStateStr = self.stateToString(initialNode.getState()) 
        reached = {initStateStr: initialNode.getCost()} #dict with all expanded nodes and their f(n) cost

        while not frontier.empty(): 
            currNode = frontier.get()[1]
            if currNode.getState() == self._goalState: # goal state has been reached
                return currNode, len(reached) # return solution node, length of reached

            # expand current node for possible moves
            children = self.expand(currNode, self._heuristic)
            for child in children:
                childState = self.stateToString(child.getState())

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

    def stateToString(self, state): 
        #convert state from list to string
        tempState = [tile for row in state for tile in row]
        output = " ".join(tempState)
        return output

    def expand(self, node, heuristic):
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
                
                action = self.determineAction(dx, dy) #action number
                newState = node.getState() 
                # perform swap
                newState[zX][zY], newState[sX][sY] = newState[sX][sY], newState[zX][zY]
                childNode = Node(newState, node, action, node.getDepth() + 1, heuristic)
                children.append(childNode)

        return children

    def determineAction(self, dx, dy):
        if dy == -1 and dx == 0: return 1     # left
        if dy == -1 and dx == -1: return 2    # up-left
        if dy == 0 and dx == -1: return 3     # up
        if dy == 1 and dx == -1: return 4     # up-right
        if dy == 1 and dx == 0: return 5      # right
        if dy == 1 and dx == 1: return 6      # down-right
        if dy == 0 and dx == 1: return 7      # down
        if dy == -1 and dx == 1: return 8     # down-left