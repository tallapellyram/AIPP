from collections import deque

class Queue:
    """Simple FIFO queue with O(1) enqueue/dequeue using deque."""
    __slots__ = ("_data",)

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Add item to the end of the queue."""
        self._data.append(item)

    def dequeue(self):
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def is_empty(self):
        """Return True if the queue is empty."""
        return not self._data


if __name__ == "__main__":
    q = Queue()
    print("Initially empty?", q.is_empty())

    for val in (10, 20, 30):
        q.enqueue(val)
        print("enqueued", val)

    print("Dequeuing all items:")
    while not q.is_empty():
        print("dequeue ->", q.dequeue())

    try:
        q.dequeue()
    except IndexError as e:
        print("dequeue error:", e)