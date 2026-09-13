def counting_sort(arr: list[int]) -> list[int]:
    """
    Create and return a new list sorted in ascending order
    by applying the Counting Sort algorithm to the given list
    that contains only non-negative integers.
    """

    n = len(arr)
    if n == 0:
        return []

    max_num = max(arr)

    count = [0] * (max_num + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, max_num + 1):
        count[i] += count[i - 1]

    output = [0] * n
    i = n - 1

    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    return output


arr = [4, 2, 2, 8, 3, 3, 1, 0]

assert counting_sort(arr) == [0, 1, 2, 2, 3, 3, 4, 8]
assert arr == [4, 2, 2, 8, 3, 3, 1, 0]
