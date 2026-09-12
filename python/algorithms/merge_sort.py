def merge_sort(arr: list[int]) -> list[int]:
    """
    Create and return a new list sorted in ascending order
    using the Merge Sort algorithm without mutating the original.
    """

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


arr = [42, 37, 53, 17]

assert merge_sort(arr) == [17, 37, 42, 53]
assert arr == [42, 37, 53, 17]
