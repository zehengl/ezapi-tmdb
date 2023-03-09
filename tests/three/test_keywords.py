from utils import polite

keyword_id = 3986  # spider-man


@polite
def test_get_keyword_details(tmdb):
    assert tmdb.get_keyword_details(keyword_id) is not None


@polite
def test_get_keyword_movies(tmdb):
    assert tmdb.get_keyword_movies(keyword_id) is not None
