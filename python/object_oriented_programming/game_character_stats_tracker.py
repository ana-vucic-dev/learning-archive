class GameCharacter:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        if not name.strip():
            raise ValueError('Name cannot be empty.')
        
        self._name = name
        self._level = 1
        self._health = 100
        self._mana = 50

    @property
    def name(self) -> str:
        return self._name

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError('Health must be an integer.')
        
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError('Mana must be an integer.')
        
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self) -> int:
        return self._level

    def level_up(self) -> None:
        self._level += 1
        self.health = 100
        self.mana = 50

    def __str__(self) -> str:
        return f'Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}'


kratos = GameCharacter('Kratos')

assert str(kratos) == """Name: Kratos
Level: 1
Health: 100
Mana: 50"""

kratos.health -= 30
kratos.mana -= 10

assert kratos.health == 70
assert kratos.mana == 40

assert str(kratos) == """Name: Kratos
Level: 1
Health: 70
Mana: 40"""

kratos.level_up()

assert kratos.level == 2
assert kratos.health == 100
assert kratos.mana == 50

assert str(kratos) == """Name: Kratos
Level: 2
Health: 100
Mana: 50"""

kratos.health = -300
kratos.mana = -150

assert kratos.health == 0
assert kratos.mana == 0

assert str(kratos) == """Name: Kratos
Level: 2
Health: 0
Mana: 0"""
