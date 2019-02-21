import pytest

from . import polite

externals = [
    ("imdb_id", "tt0903747"),
    ("freebase_mid", "/m/03d34x8"),
    ("freebase_id", "en/breaking_bad"),
    ("tvdb_id", 81189),
    ("tvrage_id", 18164),
]


@polite
@pytest.mark.parametrize("is_error", [True, False])
@pytest.mark.parametrize("external_source, external_id", externals)
def test_find_by_id(tmdb, is_error, external_source, external_id):
    if is_error:
        with pytest.raises(RuntimeError):
            assert tmdb.find_by_id(external_id)
    else:
        assert tmdb.find_by_id(external_id, external_source=external_source) is not None
