def adjacency_list_to_matrix(adjacency_list: dict[int, list[int]]) -> list[list[int]]:
    """
    Convert an adjacency list of an unweighted graph
    into an adjacency matrix.
    """

    n = len(adjacency_list)
    matrix = [[0] * n for _ in range(n)]

    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    return matrix


assert adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}) == [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
