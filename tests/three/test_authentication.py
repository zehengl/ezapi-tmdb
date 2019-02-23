import os

from . import polite


@polite
def test_create_guest_session(tmdb):
    assert tmdb.create_guest_session() is not None


@polite
def test_create_request_token(tmdb):
    assert tmdb.create_request_token() is not None


@polite
def test_session_workflow_with_login(tmdb):
    username = os.getenv("username")
    password = os.getenv("password")
    request_token = tmdb.create_request_token().get("request_token")

    assert username and password and request_token
    assert tmdb.create_session_with_login(username, password, request_token)

    session_id = tmdb.create_session(request_token).get("session_id")

    assert tmdb.delete_session(session_id) is not None
