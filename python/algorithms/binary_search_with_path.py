def binary_search(search_list: list[int], target: int) -> tuple[list[int], str]:
    path_to_target = []
    left = 0
    right = len(search_list) - 1

    while left <= right:
        middle = left + (right - left) // 2
        value_at_middle = search_list[middle]
        path_to_target.append(value_at_middle)

        if target == value_at_middle:
            return path_to_target, f'Target found at index {middle}'
        elif target > value_at_middle:
            left = middle + 1
        else:
            right = middle - 1

    return [], 'Target not found'


assert binary_search([1, 2, 3, 4, 5], 3) == ([3], 'Target found at index 2')
assert binary_search([1, 2, 3, 4, 5, 9], 4) == ([3, 5, 4], 'Target found at index 3')
assert binary_search([1, 3, 5, 9, 14, 22], 10) == ([], 'Target not found')
