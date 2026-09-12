def median_of_three_with_protection(arr: list[int], left: int, right: int) -> int:
    """
    Find the median element using the Median-of-Three strategy
    and place it in the second-to-last position
    to protect it during partitioning.
    """

    middle = left + (right - left) // 2

    if arr[left] > arr[middle]:
        arr[left], arr[middle] = arr[middle], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[middle] > arr[right]:
        arr[middle], arr[right] = arr[right], arr[middle]

    arr[middle], arr[right - 1] = arr[right - 1], arr[middle]

    return arr[right - 1]


def partition(arr: list[int], left: int, right: int) -> int:
    """
    Partition the given list using
    Median-of-Three pivot selection.
    """

    pivot = median_of_three_with_protection(arr, left, right)

    i = left
    j = right - 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return i

        arr[i], arr[j] = arr[j], arr[i]


def insertion_sort(arr: list[int], left: int, right: int) -> list[int]:
    """
    Sort the given list in place in ascending order
    using the Insertion Sort algorithm
    and return the sorted list.
    """

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def quicksort_optimized(
    arr: list[int], left: int = 0, right: int | None = None
) -> list[int]:
    """
    Sort the given list in place in ascending order
    using the Quicksort algorithm with Median-of-Three pivot selection,
    a protected pivot during partitioning, an Insertion Sort fallback
    for small partitions, and tail recursion elimination.
    Return the sorted list.
    """

    if right is None:
        right = len(arr) - 1

    if len(arr) <= 1:
        return arr

    if left + 10 > right:
        return insertion_sort(arr, left, right)

    if left < right:
        pivot = partition(arr, left, right)

        if pivot - left < right - pivot:
            quicksort_optimized(arr, left, pivot - 1)
            left = pivot + 1
        else:
            quicksort_optimized(arr, pivot + 1, right)
            right = pivot - 1

    return arr


arr = [50, 2, 41, 25, 6, 3, 15]

assert quicksort_optimized(arr) == [2, 3, 6, 15, 25, 41, 50]
assert arr == [2, 3, 6, 15, 25, 41, 50]
