"""Unit tests covering Stack edge cases."""

import unittest

from stack import Stack


class StackTests(unittest.TestCase):
    def test_push_pop_maintains_lifo(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(len(stack), 1)

    def test_peek_does_not_remove(self) -> None:
        stack = Stack(["a"])
        self.assertEqual(stack.peek(), "a")
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 1)

    def test_pop_empty_raises(self) -> None:
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_empty_raises(self) -> None:
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_init_with_iterable(self) -> None:
        stack = Stack(range(3))
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(list(stack._items), [0, 1])  # type: ignore[attr-defined]


if __name__ == "__main__":
    unittest.main()


