class MediaError(Exception):
    """Incorrect media type."""

    def __init__(self, message: str, obj) -> None:
        super().__init__(message)
        self.obj = obj


class Movie:
    def __init__(
        self, title: str, year: int, directors: list[str], duration: int
    ) -> None:
        if not isinstance(title, str):
            raise TypeError('Title must be a string.')
        if not title.strip():
            raise ValueError('Title cannot be empty.')
        if not isinstance(year, int):
            raise TypeError('Release year must be an integer.')
        if year < 1895:
            raise ValueError('Release year must be 1895 or later.')
        if not isinstance(directors, list):
            raise TypeError('Director(s) must be a list.')
        if not len(directors):
            raise ValueError('At least one director is required.')
        if any(not isinstance(director, str) for director in directors):
            raise TypeError('Every director name must be of type string.')
        if any(not director.strip() for director in directors):
            raise ValueError('Director name(s) cannot be empty.')
        if not isinstance(duration, int):
            raise TypeError('Duration must be an integer.')
        if duration <= 0:
            raise ValueError('Duration must be positive.')

        self.title = title
        self.year = year
        self.directors = directors
        self.duration = duration

    def __str__(self) -> str:
        return f'{self.title} ({self.year})\nDuration: {self.duration} minutes\nDirector{"s" if len(self.directors) > 1 else ""}: {", ".join(self.directors)}\n'


class TVSeries(Movie):
    def __init__(
        self,
        title: str,
        year: int,
        directors: list[str],
        duration: int,
        seasons: int,
        total_episodes: int,
    ) -> None:
        super().__init__(title, year, directors, duration)

        if not isinstance(seasons, int) or not isinstance(total_episodes, int):
            raise TypeError('Seasons and total episodes must be integers.')
        if seasons < 1:
            raise ValueError('The number of seasons must be at least 1.')
        if total_episodes < 1:
            raise ValueError('The total number of episodes must be at least 1.')

        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self) -> str:
        return f'{self.title} ({self.year}) — {self.seasons} seasons, {self.total_episodes} episodes\nDuration: {self.duration} minutes (episode average)\nCreator{"s" if len(self.directors) > 1 else ""}: {", ".join(self.directors)}\n'


class MediaCatalogue:
    def __init__(self) -> None:
        self.items: list[Movie | TVSeries] = []

    def add(self, media_item: Movie) -> None:
        if not isinstance(media_item, Movie):
            raise MediaError(
                'This catalogue only supports instances of the Movie and TVSeries classes.',
                media_item,
            )

        self.items.append(media_item)

    def get_movies(self) -> list[Movie]:
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self) -> list[TVSeries]:
        return [item for item in self.items if isinstance(item, TVSeries)]

    def __str__(self) -> str:
        if not self.items:
            return 'Media Catalogue (empty)'

        movies = self.get_movies()
        series = self.get_tv_series()

        result = f'Media Catalogue ({len(self.items)} items):\n\n'

        if movies:
            movies_heading = ' MOVIES '
            result += f'{movies_heading:=^50}\n\n'

            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'

        if series:
            series_heading = ' TV SERIES '
            result += f'{series_heading:=^50}\n\n'

            for i, tv_series in enumerate(series, 1):
                result += f'{i}. {tv_series}\n'

        return result


catalogue = MediaCatalogue()

interstellar = Movie('Interstellar', 2014, ['Christopher Nolan'], 169)
catalogue.add(interstellar)

assert catalogue.get_movies() == [interstellar]
assert catalogue.get_tv_series() == []

the_expanse = TVSeries('The Expanse', 2015, ['Mark Fergus', 'Hawk Ostby'], 60, 6, 62)
catalogue.add(the_expanse)

assert isinstance(the_expanse, Movie)
assert isinstance(the_expanse, TVSeries)
assert catalogue.get_tv_series() == [the_expanse]

assert 'Interstellar (2014)' in str(interstellar)
assert 'The Expanse (2015)' in str(the_expanse)
assert '6 seasons, 62 episodes' in str(the_expanse)
