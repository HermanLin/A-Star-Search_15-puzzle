# Node class for A-Star Search Algorithm

class Node:

    def __init__(self, state, parent, action, cost):
        self._state = state
        self._parent = None
        self._action = None
        self._cost = None

    def getValuePos(self, value):
        for i in range(4):
            for j in range(4):
                if self._state[i][j] == value:
                    return i, j