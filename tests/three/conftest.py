import os

import pytest

from tmdb.three import TMDb


@pytest.fixture(scope="module")
def tmdb():
    api_key = os.getenv("api_key", None)

    return TMDb(api_key) if api_key else None
