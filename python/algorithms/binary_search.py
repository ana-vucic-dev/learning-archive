def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return -1


assert binary_search([1, 2, 3, 4, 5], 2) == 1
assert binary_search([2, 3, 5, 7, 11, 13, 17, 23], 17) == 6
assert binary_search([25, 46, 82, 123], 5) == -1
