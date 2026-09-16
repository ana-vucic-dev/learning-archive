def tower_of_hanoi(n: int) -> str:
    """
    Solve the Tower of Hanoi puzzle for `n` disks
    and return the sequence of rod states.
    """

    rods: dict[str, list[int]] = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': [],
    }

    path = []

    def update_path() -> None:
        current_state = f'{rods["A"]} {rods["B"]} {rods["C"]}'
        path.append(current_state)

    update_path()

    def move(disk_count: int, source: str, target: str, auxiliary: str) -> None:
        if disk_count == 1:
            rods[target].append(rods[source].pop())
            update_path()
        else:
            move(disk_count - 1, source, auxiliary, target)
            rods[target].append(rods[source].pop())
            update_path()
            move(disk_count - 1, auxiliary, target, source)

    move(n, 'A', 'C', 'B')
    return '\n'.join(path)


assert tower_of_hanoi(1) == '[1] [] []\n[] [] [1]'

result = tower_of_hanoi(3)

assert result.splitlines()[0] == '[3, 2, 1] [] []'
assert result.splitlines()[-1] == '[] [] [3, 2, 1]'
assert len(result.splitlines()) == 8
