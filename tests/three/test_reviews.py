from . import polite

review_id = "578193f29251417c28001764"


@polite
def test_get_review_details(tmdb):
    assert tmdb.get_review_details(review_id) is not None
