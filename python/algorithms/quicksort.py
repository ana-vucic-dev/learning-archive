def quicksort(arr: list[int]) -> list[int]:
    """
    Create and return a new list sorted in ascending order
    using the Quicksort algorithm without mutating the original.
    """

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


arr = [50, 2, 41, 25, 6, 3, 15]

assert quicksort(arr) == [2, 3, 6, 15, 25, 41, 50]
assert arr == [50, 2, 41, 25, 6, 3, 15]
