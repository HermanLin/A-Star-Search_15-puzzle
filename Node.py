# Node class for A-Star Search Algorithm

class Node:

    def __init__(self, state, parent, action, cost):
        self._state = state
        self._parent = parent
        self._action = action
        self._cost = cost

    def getCost(self):
        return self._cost

    def getValuePos(self, value):
        for i in range(4):
            for j in range(4):
                if self._state[i][j] == value:
                    return i, j