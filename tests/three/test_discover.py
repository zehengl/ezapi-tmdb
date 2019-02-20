from . import polite


@polite
def test_get_movie_discover(tmdb):
    assert tmdb.get_movie_discover() is not None


@polite
def test_get_tv_discover(tmdb):
    assert tmdb.get_tv_discover() is not None
