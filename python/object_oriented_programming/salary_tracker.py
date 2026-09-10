class Employee:
    _base_salaries: dict[str, int] = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name: str, level: str) -> None:
        if not isinstance(name, str) or not isinstance(level, str):
            raise TypeError('Employee name and level must be strings.')
        if not name.strip() or not level.strip():
            raise ValueError('Employee name and level cannot be empty.')

        self.name = name
        self.level = level
        self.salary = Employee._base_salaries[level]

    def __str__(self) -> str:
        return f'{self.name}: {self.level}'

    def __repr__(self) -> str:
        return f"Employee('{self.name}', '{self.level}')"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError('Employee name must be a string.')
        if not new_name.strip():
            raise ValueError('Employee name cannot be empty.')

        self._name = new_name

    @property
    def level(self) -> str:
        return self._level

    @level.setter
    def level(self, new_level: str) -> None:
        if not isinstance(new_level, str):
            raise TypeError('Employee level must be a string.')

        if new_level not in Employee._base_salaries:
            raise ValueError(f'Invalid value "{new_level}" for the "level" attribute.')

        if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(f'"{self.level}" is already the selected level.')

        if (
            hasattr(self, '_level')
            and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]
        ):
            raise ValueError('Downgrading an employee level is not allowed.')

        self.salary = Employee._base_salaries[new_level]
        self._level = new_level

    @property
    def salary(self) -> int:
        return self._salary

    @salary.setter
    def salary(self, new_salary: int) -> None:
        if not isinstance(new_salary, int):
            raise TypeError('Employee salary must be an integer.')

        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(
                f'Salary must be higher than the minimum {self.level} salary of ${Employee._base_salaries[self.level]}.'
            )

        self._salary = new_salary


alice_smith = Employee('alice smith', 'trainee')

alice_smith.name = 'Alice Smith'

assert str(alice_smith) == 'Alice Smith: trainee'
assert repr(alice_smith) == "Employee('Alice Smith', 'trainee')"
assert alice_smith.salary == 1000

alice_smith.level = 'junior'

assert alice_smith.salary == 2000
assert str(alice_smith) == 'Alice Smith: junior'
