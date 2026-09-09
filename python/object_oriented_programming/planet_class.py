class Planet:
    def __init__(self, name: str, planet_type: str, star: str) -> None:
        if (
            not isinstance(name, str)
            or not isinstance(planet_type, str)
            or not isinstance(star, str)
        ):
            raise TypeError("The planet's name, type, and star must be strings.")

        if name.strip() == '' or planet_type.strip() == '' or star.strip() == '':
            raise ValueError("The planet's name, type, and star cannot be empty.")

        self.name = name.strip()
        self.planet_type = planet_type.strip()
        self.star = star.strip()

    def orbit(self) -> str:
        return f'{self.name} orbits the {self.star}.'

    def __str__(self) -> str:
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


planet_1 = Planet('Earth', 'Terrestrial', 'Sun')
planet_2 = Planet('Jupiter', 'Gas Giant', 'Sun')
planet_3 = Planet('Proxima Centauri b', 'Terrestrial', 'Proxima Centauri')

assert planet_1.orbit() == 'Earth orbits the Sun.'
assert str(planet_2) == 'Planet: Jupiter | Type: Gas Giant | Star: Sun'
