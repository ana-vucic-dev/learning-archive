def counting_sort_reconstruct(arr: list[int]) -> list[int]:
    """
    Sort the given list of non-negative integers
    in ascending order using Counting Sort by
    reconstructing it using each integer's frequency.
    Return a new sorted list without mutating the original.
    """

    n = len(arr)
    if n == 0:
        return []

    max_num = max(arr)
    count = [0] * (max_num + 1)

    for num in arr:
        count[num] += 1

    output = [0] * n
    i = 0

    for num in range(len(count)):
        for _ in range(count[num]):
            output[i] = num
            i += 1

    return output


arr = [4, 2, 2, 8, 3, 3, 1, 0]

assert counting_sort_reconstruct(arr) == [0, 1, 2, 2, 3, 3, 4, 8]
assert arr == [4, 2, 2, 8, 3, 3, 1, 0]
