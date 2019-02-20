import pytest

from . import polite

search_types = ["company", "collection", "keyword", "movie", "multi", "person", "tv"]
search_kwargs = [({}, True), ({"query": "titanic"}, False)]


@polite
@pytest.mark.parametrize("search_type", search_types)
@pytest.mark.parametrize("kwargs, is_error", search_kwargs)
def test_get_search(tmdb, search_type, kwargs, is_error):
    method = getattr(tmdb, f"get_{search_type}_search")
    if is_error:
        with pytest.raises(RuntimeError):
            method(**kwargs)
    else:
        assert method(**kwargs) is not None
