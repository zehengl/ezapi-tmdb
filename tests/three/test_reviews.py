from . import polite


@polite
def test_get_review_details(tmdb):
    assert tmdb.get_review_details("578193f29251417c28001764") is not None
