"""Stack data structure implementation.

Initial skeleton generated via GitHub Copilot using the prompt:
'Create a Python Stack class with push, pop, and peek methods.'
Additional validation, helpers, and docs were added manually.
"""

from __future__ import annotations

from typing import Generic, Iterable, List, Optional, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """Simple LIFO stack with optional iterable initialization."""

    def __init__(self, items: Optional[Iterable[T]] = None) -> None:
        self._items: List[T] = list(items) if items is not None else []

    def push(self, item: T) -> None:
        """Push a value on top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top value."""
        if not self._items:
            raise IndexError("pop from empty Stack")
        return self._items.pop()

    def peek(self) -> T:
        """Return the top value without removing it."""
        if not self._items:
            raise IndexError("peek from empty Stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True when the stack has no elements."""
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"


