import os
import sys

import pytest
from dotenv import load_dotenv

from tmdb.three import TMDb

sys.path.append(os.path.join(os.path.dirname(__file__), "helpers"))
load_dotenv()


@pytest.fixture(scope="module")
def tmdb():
    api_key = os.getenv("tmdb_api_key", None)

    return TMDb(api_key) if api_key else None


@pytest.fixture(scope="module")
def session_id(tmdb):
    username = os.getenv("tmdb_username")
    password = os.getenv("tmdb_password")
    request_token = tmdb.create_request_token().get("request_token")

    tmdb.create_session_with_login(username, password, request_token)

    session_id = tmdb.create_session(request_token).get("session_id")

    yield session_id

    tmdb.delete_session(session_id)


@pytest.fixture(scope="module")
def account_id(tmdb, session_id):
    return tmdb.get_account_details(session_id=session_id).get("id")
