import pytest
from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "Movie1"

    def test_create(self):
        movie_data = {
            "title": "Movie4",
            "description": "description4",
            "trailer": "trailer4",
            "year": 2004,
            "rating": 10.4,
            "genre_id": 4,
            "director_id": 4
        }

        movie = self.movie_service.create(movie_data)
        assert movie.id is not None

    def test_update(self):
        movie_data = {
            "id": 3,
            "title": "Movie3_update",
            "description": "desc_update",
            "trailer": "link_update",
            "year": 666,
            "rating": 66.6,
            "director_id": 666,
            "genre_id": 666
        }
        assert self.movie_service.update(movie_data)

    def test_delete(self):
        assert self.movie_service.delete(1) is None



