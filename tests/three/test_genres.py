from . import polite


@polite
def test_get_movie_genre_list(tmdb):
    assert tmdb.get_movie_genre_list() is not None


@polite
def test_get_tv_genre_list(tmdb):
    assert tmdb.get_tv_genre_list() is not None
