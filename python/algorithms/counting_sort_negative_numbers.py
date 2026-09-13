def counting_sort_negative_numbers(arr: list[int]) -> list[int]:
    """
    Sort the given list (which may contain negative integers)
    in ascending order using Counting Sort with
    `O(k)` space complexity, where `k` is the range of values
    from the minimum to the maximum integer,
    and return the sorted list.
    """

    if len(arr) <= 1:
        return arr

    max_num = max(arr)
    min_num = min(arr)

    offset = 0 - min_num
    count = [0] * (max_num + 1 + offset)

    for num in arr:
        count[num + offset] += 1

    i = 0
    for num, frequency in enumerate(count):
        while frequency > 0:
            arr[i] = num - offset
            i += 1
            frequency -= 1

    return arr


arr = [4, -2, 2, 8, 0, 3, -3, 1]

assert counting_sort_negative_numbers(arr) == [-3, -2, 0, 1, 2, 3, 4, 8]
assert arr == [-3, -2, 0, 1, 2, 3, 4, 8]
