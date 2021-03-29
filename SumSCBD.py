from Node import Node

class SumSCBD:

    # Class for easy heuristic calculation
    # - stores the goal state and calculates the SCBD according to it

    def __init__(self, state):
        self._goalNode = Node(state, None, None, None)

    def calc_SCBD(self, node):
        # calculate heuristic using sum of chessboard distances
        # - chessboard distance = max(horizontal moves, vertical moves)

        sum_SCBD = 0
        for i in range(16):
            # find tile positions
            goalX, goalY = self._goalNode.getValuePos(i)
            currX, currY = node.getValuePos(i)
            # add the max between hori/vert moves
            sum_SCBD += max(abs(goalX - currX), abs(goalY - currY))
        return sum_SCBD