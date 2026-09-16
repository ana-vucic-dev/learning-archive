INF = float('inf')


def dijkstra(
    matrix: list[list[float]], start_node: int
) -> tuple[list[float], list[list[int]]]:
    """
    Implement Dijkstra's algorithm using an adjacency matrix
    and return the shortest distances and paths from the start node.
    """

    n = len(matrix)
    distances = [INF] * n
    distances[start_node] = 0
    paths = [[node] for node in range(n)]
    visited = [False] * n

    for _ in range(n):
        min_distance = INF
        current = -1

        for node in range(n):
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                current = node

        if current == -1:
            break

        visited[current] = True

        for neighbor in range(n):
            distance = matrix[current][neighbor]

            if distance != INF and not visited[neighbor]:
                new_distance = distances[current] + distance

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    paths[neighbor] = paths[current] + [neighbor]

    return distances, paths


adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0]
]


distances, paths = dijkstra(adj_matrix, 0)

assert distances == [0, 4, 3, 4, 8, 6]
assert paths == [
    [0],
    [0, 2, 1],
    [0, 2],
    [0, 2, 3],
    [0, 2, 4],
    [0, 2, 1, 5]
]

distances, paths = dijkstra(adj_matrix, 3)

assert distances[0] == 4
assert paths[0] == [3, 2, 0]

assert distances[4] == 6
assert paths[4] == [3, 2, 4]
