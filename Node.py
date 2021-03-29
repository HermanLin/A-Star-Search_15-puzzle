import copy 

class Node:
    # Node class for A-Star Search Algorithm

    def __init__(self, state, parent, action, cost):
        self._state = state
        self._parent = parent
        self._action = action
        self._cost = cost

    def getState(self):
        return copy.deepcopy(self._state)

    def getCost(self):
        return self._cost

    def getValuePos(self, value):
        for i in range(4):
            for j in range(4):
                if self._state[i][j] == value:
                    return i, j