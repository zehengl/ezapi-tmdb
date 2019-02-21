from . import polite

credit_id = "52542282760ee313280017f9"


@polite
def test_get_credit_details(tmdb):
    assert tmdb.get_credit_details(credit_id) is not None
