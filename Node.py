# Node class for A-Star Search Algorithm

class Node:

    def __init__(self, state, moves):
        self._state = state
        self._moves = moves
        self._hValue = None

    def getGValue(self):
        # cost of getting to current state (1 per move)
        return len(self._moves)

    def getHValue(self):
        # if _hValue == None: calculate heuristic

        return self._hValue

    def getFValue(self):
        # f(n) = g(n) + h(n)

        return self.getGValue() + self.getHValue()

    def getMoves(self):
        return self._moves

    def getValuePos(self, value):
        for i in range(4):
            for j in range(4):
                if self._state[i][j] == value:
                    return i, j