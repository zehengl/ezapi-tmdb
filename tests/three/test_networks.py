from . import polite


@polite
def test_get_network_details(tmdb):
    assert tmdb.get_network_details(16) is not None


@polite
def test_get_network_alternative_names(tmdb):
    assert tmdb.get_network_alternative_names(16) is not None


@polite
def test_get_network_images(tmdb):
    assert tmdb.get_network_images(16) is not None
