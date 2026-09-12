def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sort the given list in place in ascending order
    using the Bubble Sort algorithm
    and return the sorted list.
    """

    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

assert bubble_sort(arr) == [11, 12, 22, 25, 34, 64, 90]
assert arr == [11, 12, 22, 25, 34, 64, 90]
