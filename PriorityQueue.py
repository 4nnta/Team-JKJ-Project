import heapq

class PriorityQueue(object):

    """
    Combined priority queue and set data structure.

    Acts like a priority queue, except that its items are guaranteed to be
    unique. Provides O(1) membership test, O(log N) insertion and O(log N)
    removal of the smallest item.

    Important: the items of this data structure must be both comparable and
    hashable (i.e. must implement __cmp__ and __hash__). This is true of
    Python's built-in objects, but you should implement those methods if you
    want to use the data structure for custom objects.
    """

    def __init__(self, items = []):
        """
        Create a new PriorityQueueSet.

        Arguments:
            items (list): An initial item list - it can be unsorted and
                non-unique. The data structure will be created in O(N).
        """
        self.heap = items
        heapq.heapify(self.heap)

    def size(self):
        return len(self.heap)

    def pop(self):
        """Remove and return the smallest item from the queue."""
        smallest = heapq.heappop(self.heap)
        return smallest

    def add(self, item):
        heapq.heappush(self.heap, item)

    """
    PriorityQueue data structure code taken from Stack Overflow
    """