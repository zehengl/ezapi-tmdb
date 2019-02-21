from . import polite

network_id = 16  # CBS


@polite
def test_get_network_details(tmdb):
    assert tmdb.get_network_details(network_id) is not None


@polite
def test_get_network_alternative_names(tmdb):
    assert tmdb.get_network_alternative_names(network_id) is not None


@polite
def test_get_network_images(tmdb):
    assert tmdb.get_network_images(network_id) is not None
