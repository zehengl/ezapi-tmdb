from . import polite


@polite
def test_get_keyword_details(tmdb):
    assert tmdb.get_keyword_details(3586) is not None


@polite
def test_get_keyword_movies(tmdb):
    assert tmdb.get_keyword_movies(3586) is not None
