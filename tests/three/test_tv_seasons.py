import pytest

from . import polite


tv_id = 1418  # The Big Bang Theory
season_number = 12


@polite
def test_get_tv_season_details(tmdb):
    assert tmdb.get_tv_season_details(tv_id, season_number) is not None


@polite
def test_get_tv_season_account_states(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.get_tv_season_account_states(tv_id, season_number)


@polite
def test_get_tv_season_changes(tmdb):
    assert tmdb.get_tv_season_changes(season_number) is not None


@polite
def test_get_tv_season_credits(tmdb):
    assert tmdb.get_tv_season_credits(tv_id, season_number) is not None


@polite
def test_get_tv_season_external_ids(tmdb):
    assert tmdb.get_tv_season_external_ids(tv_id, season_number) is not None


@polite
def test_get_tv_season_images(tmdb):
    assert tmdb.get_tv_season_images(tv_id, season_number) is not None


@polite
def test_get_tv_season_videos(tmdb):
    assert tmdb.get_tv_season_videos(tv_id, season_number) is not None
