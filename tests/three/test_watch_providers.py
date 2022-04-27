from . import polite


@polite
def test_get_available_regions(tmdb):
    assert tmdb.get_available_regions() is not None


@polite
def test_get_movie_providers(tmdb):
    assert tmdb.get_movie_providers() is not None


@polite
def test_get_tv_providers(tmdb):
    assert tmdb.get_tv_providers() is not None
