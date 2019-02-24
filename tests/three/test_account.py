import pytest

from . import polite

media_type, media_id = "movie", 550


@polite
def test_get_account_details(tmdb, session_id):
    assert tmdb.get_account_details(session_id=session_id) is not None


@polite
def test_get_account_lists(tmdb, account_id, session_id):
    assert tmdb.get_account_lists(account_id, session_id=session_id) is not None


@polite
def test_get_account_favorite_movies(tmdb, account_id, session_id):
    assert (
        tmdb.get_account_favorite_movies(account_id, session_id=session_id) is not None
    )


@polite
def test_get_account_favorite_tvs(tmdb, account_id, session_id):
    assert tmdb.get_account_favorite_tvs(account_id, session_id=session_id) is not None


@polite
@pytest.mark.parametrize("favorite", [True, False])
def test_mark_as_favorite(tmdb, account_id, session_id, favorite):
    assert (
        tmdb.mark_as_favorite(
            account_id, media_type, media_id, favorite, session_id=session_id
        )
        is not None
    )


@polite
def test_get_account_rated_movies(tmdb, account_id, session_id):
    assert tmdb.get_account_rated_movies(account_id, session_id=session_id) is not None


@polite
def test_get_account_rated_tvs(tmdb, account_id, session_id):
    assert tmdb.get_account_rated_tvs(account_id, session_id=session_id) is not None


@polite
def test_get_account_rated_tv_episodes(tmdb, account_id, session_id):
    assert (
        tmdb.get_account_rated_tv_episodes(account_id, session_id=session_id)
        is not None
    )


@polite
def test_get_account_movie_watchlist(tmdb, account_id, session_id):
    assert (
        tmdb.get_account_movie_watchlist(account_id, session_id=session_id) is not None
    )


@polite
def test_get_account_tv_watchlist(tmdb, account_id, session_id):
    assert tmdb.get_account_tv_watchlist(account_id, session_id=session_id) is not None


@polite
@pytest.mark.parametrize("watchlist", [True, False])
def test_add_to_watchlist(tmdb, account_id, session_id, watchlist):
    assert (
        tmdb.add_to_watchlist(
            account_id, media_type, media_id, watchlist, session_id=session_id
        )
        is not None
    )
