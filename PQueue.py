import copy

class PQueue:
    # Unique implementation of a PriorityQueue for 15-puzzle Nodes

    def __init__(self):
        self._queue = []

    def print(self):
        return copy.deepcopy(self._queue)

    def empty(self):
        return len(self._queue) == 0

    def get(self):
        ind = 0
        smallestFValue = self._queue[ind][0]
        
        for elem in self._queue:
            if elem[0] < smallestFValue:
                smallestFValue = elem[0]
                ind = self._queue.index(elem)
        
        return self._queue.pop(ind)

    def put(self, element):
        # element is a tuple of (f(n), Node)
        return self._queue.append(element)