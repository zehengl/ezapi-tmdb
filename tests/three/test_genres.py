def test_get_movie_discover(tmdb):
    assert tmdb.get_movie_genre_list() is not None


def test_get_tv_discover(tmdb):
    assert tmdb.get_tv_genre_list() is not None
