import copy 

class Node:
    # Node class for A-Star Search Algorithm

    def __init__(self, state, parent, action, depth, heuristic):
        self._state = state
        self._parent = parent
        self._action = action 
        self._depth = depth
        self._heuristic = heuristic
        self._cost = None

    def getState(self):
        return copy.deepcopy(self._state)

    def getParent(self):
        return self._parent

    def getAction(self):
        return self._action

    def getDepth(self):
        return self._depth

    def getCost(self):
        if not self._cost: # calculate if the cost has not been set
            self._cost = self._depth + self._heuristic.calc_SCBD(self)
        return self._cost

    def getValuePos(self, value):
        for i in range(4):
            for j in range(4):
                if self._state[i][j] == str(value):
                    return i, j