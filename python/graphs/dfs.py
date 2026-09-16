def dfs(adjacency_matrix: list[list[int]], root: int) -> list[int]:
    """
    Return all the nodes reachable from the specified `root` node
    in the given graph represented by an adjacency matrix.
    """

    if root < 0 or root >= len(adjacency_matrix):
        return []

    stack = [root]
    visited = set()
    reachable_nodes = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            reachable_nodes.append(node)

            neighbors = adjacency_matrix[node]
            n = len(neighbors)

            for i in range(n - 1, -1, -1):
                if neighbors[i] == 1 and i not in visited:
                    stack.append(i)

    return reachable_nodes


assert dfs([
    [0, 1, 0, 0], 
    [1, 0, 1, 0], 
    [0, 1, 0, 1], 
    [0, 0, 1, 0]
  ], 1) == [1, 0, 2, 3]
