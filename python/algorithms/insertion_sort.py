def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sort the given list in place in ascending order
    using the Insertion Sort algorithm
    and return the sorted list.
    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [91, 5, 14, 43, 3]

assert insertion_sort(arr) == [3, 5, 14, 43, 91]
assert arr == [3, 5, 14, 43, 91]
