from . import polite


@polite
def test_get_movie_change_list(tmdb):
    assert tmdb.get_movie_change_list() is not None


@polite
def test_get_tv_change_list(tmdb):
    assert tmdb.get_tv_change_list() is not None


@polite
def test_get_person_change_list(tmdb):
    assert tmdb.get_person_change_list() is not None
