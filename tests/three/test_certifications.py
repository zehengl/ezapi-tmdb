def test_get_movie_certifications(tmdb):
    assert tmdb.get_movie_certifications() is not None


def test_get_tv_certifications(tmdb):
    assert tmdb.get_tv_certifications() is not None
