def partition_lomuto(arr: list[int], left: int, right: int) -> int:
    """
    Partition the given list using the Lomuto scheme
    and return the pivot index.
    """

    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i


def quicksort_lomuto(
    arr: list[int], left: int = 0, right: int | None = None
) -> list[int]:
    """
    Sort the given list in place in ascending order
    using the Quicksort algorithm and the Lomuto
    partitioning scheme and return the sorted list.
    """

    if right is None:
        right = len(arr) - 1

    if left >= right:
        return arr

    pivot_index = partition_lomuto(arr, left, right)
    quicksort_lomuto(arr, left, pivot_index - 1)
    quicksort_lomuto(arr, pivot_index + 1, right)

    return arr


arr = [50, 2, 41, 25, 6, 3, 15]

assert quicksort_lomuto(arr) == [2, 3, 6, 15, 25, 41, 50]
assert arr == [2, 3, 6, 15, 25, 41, 50]
