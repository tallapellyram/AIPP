class Stack:
    """Lightweight LIFO stack optimized with __slots__."""
    __slots__ = ("_data",)

    def __init__(self):
        self._data: list = []

    def push(self, item):
        """Push item onto the stack (O(1))."""
        self._data.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Return the top item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        """Return True if the stack is empty."""
        return not self._data


if __name__ == "__main__":
    s = Stack()
    print("Initially empty?", s.is_empty())

    for val in (10, 20, 30):
        s.push(val)
        print(f"pushed {val}, peek -> {s.peek()}")

    print("Popping all items:")
    while not s.is_empty():
        print("pop ->", s.pop())

    # show errors for operations on empty stack
    try:
        s.peek()
    except IndexError as e:
        print("peek error:", e)

    try:
        s.pop()
    except IndexError as e:
        print("pop error:", e)


