def partition_hoare(arr: list[int], left: int, right: int) -> int:
    """
    Partition the given list using the Hoare scheme
    and return the pivot index.
    """

    pivot = arr[left + (right - left) // 2]
    i = left - 1
    j = right + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def median_of_three(arr: list[int], left: int, right: int) -> None:
    """
    Find and place the median element
    in the middle of the given list
    so the Hoare scheme can use it as the pivot.
    """

    middle = left + (right - left) // 2

    if arr[left] > arr[middle]:
        arr[left], arr[middle] = arr[middle], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[middle] > arr[right]:
        arr[middle], arr[right] = arr[right], arr[middle]


def quicksort_median_of_three(
    arr: list[int], left: int = 0, right: int | None = None
) -> list[int]:
    """
    Sort the given list in place in ascending order
    using the Quicksort algorithm that implements
    the Median-of-Three approach and the Hoare
    partitioning scheme and return the sorted list.
    """

    if right is None:
        right = len(arr) - 1

    if left >= right:
        return arr

    median_of_three(arr, left, right)
    pivot_index = partition_hoare(arr, left, right)

    quicksort_median_of_three(arr, left, pivot_index)
    quicksort_median_of_three(arr, pivot_index + 1, right)

    return arr


arr = [50, 2, 41, 25, 6, 3, 15]

assert quicksort_median_of_three(arr) == [2, 3, 6, 15, 25, 41, 50]
assert arr == [2, 3, 6, 15, 25, 41, 50]
