# Node class for A-Star Search Algorithm

class Node:

    def __init__(self, state, moves):
        self._state = state # always 4 by 4
        self._moves = moves    

    def getValuePos(self, value):
        for i in range(4):
            for j in range(4):
                if self._state[i][j] == value:
                    return i, j
                    