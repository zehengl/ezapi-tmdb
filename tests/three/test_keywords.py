from . import polite

keyword_id = 3586  # tv station


@polite
def test_get_keyword_details(tmdb):
    assert tmdb.get_keyword_details(keyword_id) is not None


@polite
def test_get_keyword_movies(tmdb):
    assert tmdb.get_keyword_movies(keyword_id) is not None
