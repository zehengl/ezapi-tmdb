from . import polite

collection_id = 86311  # The Avengers Collection


@polite
def test_get_collection_details(tmdb):
    assert tmdb.get_collection_details(collection_id) is not None


@polite
def test_get_collection_images(tmdb):
    assert tmdb.get_collection_images(collection_id) is not None


@polite
def test_get_collection_translations(tmdb):
    assert tmdb.get_collection_translations(collection_id) is not None
