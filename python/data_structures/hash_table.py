from typing import Any


class HashTable:
    def __init__(self) -> None:
        self.collection = {}

    def hash(self, key: str) -> int:
        return sum(ord(char) for char in key)

    def add(self, key: str, value: Any) -> None:
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key] = {key: value}

    def remove(self, key: str) -> None:
        hashed_key = self.hash(key)

        if hashed_key not in self.collection or key not in self.collection[hashed_key]:
            return
        del self.collection[hashed_key][key]

    def find(self, key: str) -> Any | None:
        hashed_key = self.hash(key)

        if hashed_key not in self.collection or key not in self.collection[hashed_key]:
            return None
        return self.collection[hashed_key][key]


hash_table = HashTable()

assert hash_table.hash('earth') == 532
assert hash_table.find('earth') is None

hash_table.add('earth', 'planet')

assert hash_table.find('earth') == 'planet'
assert hash_table.collection == {532: {'earth': 'planet'}}

hash_table.add('heart', 'organ')

assert hash_table.hash('heart') == 532
assert hash_table.collection == {532: {'earth': 'planet', 'heart': 'organ'}}

hash_table.add('coordinates', (1, 2))

assert hash_table.find('coordinates') == (1, 2)

hash_table.add(
    'planets',
    ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
)

assert hash_table.find('planets')[4] == 'Jupiter'

assert hash_table.remove('planet') is None

hash_table.remove('heart')
assert hash_table.find('heart') is None
