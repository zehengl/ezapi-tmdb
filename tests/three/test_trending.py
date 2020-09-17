from itertools import product

import pytest

from . import polite

media_types = ["all", "movie", "tv", "person"]
time_windows = ["day", "week"]


@polite
@pytest.mark.parametrize("media_type, time_window", product(media_types, time_windows))
def test_get_trending(tmdb, media_type, time_window):
    assert tmdb.get_trending(media_type, time_window) is not None


@polite
@pytest.mark.parametrize("media_type, time_window", product(media_types, time_windows))
def test_get_trending_de(tmdb, media_type, time_window):
    tmdb.set_options(language="de", region="de")
    assert tmdb.options
    assert tmdb.get_trending(media_type, time_window) is not None

    tmdb.reset_options()
    assert not tmdb.options
    assert tmdb.get_trending(media_type, time_window) is not None
