import pytest

from . import polite


@polite
def test_get_guest_session_rated_movies(tmdb):
    guest_session_id = tmdb.create_guest_session().get("guest_session_id")
    assert tmdb.get_guest_session_rated_movies(guest_session_id) is not None


@polite
def test_get_guest_session_rated_tvs(tmdb):
    guest_session_id = tmdb.create_guest_session().get("guest_session_id")
    assert tmdb.get_guest_session_rated_tvs(guest_session_id) is not None


@polite
def test_get_guest_session_rated_tv_episodes(tmdb):
    guest_session_id = tmdb.create_guest_session().get("guest_session_id")
    assert tmdb.get_guest_session_rated_tv_episodes(guest_session_id) is not None
