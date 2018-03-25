#works !

from Queue import LifoQueue
from collections import deque
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

def stream_med(array):

    re = []
    left = PriorityQueue()
    right = []

    for e in array:
        left.push(e, e)
        com1 = left.pop()

        heapq.heappush(right, com1)
        com2 = heapq.heappop(right)

        if len(left._queue) == len(right):
            left.push(com2, com2)
            re.append(com2)


        elif len(left._queue) > len(right):
            com3 = left.pop()
            re.append( (com3 + com2 ) /2.0 )

            left.push(com3, com3)
            heapq.heappush(right, com2)

        else:
            com3 = heapq.heappop(right)
            re.append( (com3 + com2) / 2.0)

            left.push(com2)
            heapq.heappush(right, com3)
    return re

if __name__ == "__main__":
    a = [4,1,2,3]
    print stream_med(a)
