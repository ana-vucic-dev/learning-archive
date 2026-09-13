def counting_sort_optimized_in_place(arr: list[int]) -> list[int]:
    """
    Sort the given list of non-negative integers
    in ascending order using Counting Sort with
    `O(k)` space complexity, where `k` is the
    maximum number in the list, and return the sorted list.
    """

    if len(arr) <= 1:
        return arr

    max_num = max(arr)
    count = [0] * (max_num + 1)

    for num in arr:
        count[num] += 1

    i = 0
    for num in range(len(count)):
        for _ in range(count[num]):
            arr[i] = num
            i += 1

    return arr


arr = [4, 2, 2, 8, 3, 3, 1, 0]

assert counting_sort_optimized_in_place(arr) == [0, 1, 2, 2, 3, 3, 4, 8]
assert arr == [0, 1, 2, 2, 3, 3, 4, 8]
