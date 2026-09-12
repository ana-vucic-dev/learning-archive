def selection_sort(arr: list[int]) -> list[int]:
    """
    Sort the given list in place in ascending order
    using the Selection Sort algorithm
    and return the sorted list.
    """

    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]

assert selection_sort(arr) == [11, 12, 22, 25, 64]
assert arr == [11, 12, 22, 25, 64]
