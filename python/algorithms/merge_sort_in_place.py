def merge_sort(arr: list[int]) -> None:
    """
    Sort the given list in place in ascending order
    using the Merge Sort algorithm.
    """

    if len(arr) <= 1:
        return

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [13, 56, 21, 4, 98, 7, 12]
merge_sort(arr)

assert arr == [4, 7, 12, 13, 21, 56, 98]
