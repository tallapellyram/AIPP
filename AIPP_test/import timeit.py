import timeit
import random


# -------------------------------
#  Reverse List Implementations
# -------------------------------

def reverse_list_slice(lst):
    """Reverse using slicing."""
    return lst[::-1]


def reverse_list_builtin(lst):
    """Reverse using the built-in reversed()"""
    return list(reversed(lst))


def reverse_list_two_pointer(lst):
    """Reverse using manual two-pointer swap."""
    arr = lst[:]  # avoid modifying original
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def reverse_list_inplace(lst):
    """Reverse using list.reverse() but avoid modifying the input."""
    arr = lst[:]
    arr.reverse()
    return arr


def reverse_list_loop(lst):
    """Reverse by manually building a new list."""
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result


# -------------------------------
#  Benchmarking
# -------------------------------

def run_benchmarks():
    # Create a list to test
    lst = list(range(10_000))

    setup_code = """
from __main__ import (
    reverse_list_slice,
    reverse_list_builtin,
    reverse_list_two_pointer,
    reverse_list_inplace,
    reverse_list_loop,
    lst
)
"""

    tests = {
        "Slice": "reverse_list_slice(lst)",
        "Builtin reversed()": "reverse_list_builtin(lst)",
        "Two-pointer": "reverse_list_two_pointer(lst)",
        "In-place .reverse()": "reverse_list_inplace(lst)",
        "Loop append": "reverse_list_loop(lst)",
    }

    print("\nBenchmark Results (lower = faster)\n-----------------------------------")
    for name, stmt in tests.items():
        t = timeit.timeit(stmt, setup=setup_code, number=1000)
        print(f"{name:20s}: {t:.5f} seconds")


# -------------------------------
#  Main Execution
# -------------------------------

if __name__ == "__main__":
    print("Testing correctness...")
    test_list = [1, 2, 3, 4]

    print("Slice:              ", reverse_list_slice(test_list))
    print("Builtin reversed(): ", reverse_list_builtin(test_list))
    print("Two-pointer:        ", reverse_list_two_pointer(test_list))
    print("In-place reverse(): ", reverse_list_inplace(test_list))
    print("Loop:               ", reverse_list_loop(test_list))

    run_benchmarks()
