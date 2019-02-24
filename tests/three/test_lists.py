import os
import random
import time

import pytest

from . import polite

list_id = 14151
movie_id = 597


@polite
def test_get_list_details(tmdb):
    assert tmdb.get_list_details(list_id) is not None


@polite
@pytest.mark.parametrize("is_error", [True, False])
def test_get_list_item_status(tmdb, is_error):
    if is_error:
        with pytest.raises(RuntimeError):
            tmdb.get_list_item_status(list_id)
    else:
        assert tmdb.get_list_item_status(list_id, movie_id=movie_id) is not None


@polite
def test_list_operations(tmdb, session_id):
    list_id = tmdb.create_list("test_list", session_id=session_id).get("list_id")

    assert tmdb.add_movie(list_id, movie_id, session_id=session_id) is not None

    assert tmdb.remove_movie(list_id, movie_id, session_id=session_id) is not None

    assert tmdb.clear_list(list_id, session_id=session_id, confirm=True)

    try:
        tmdb.delete_list(list_id, session_id=session_id)
    except:
        # internal error happens quite often
        pass

    assert tmdb.delete_session(session_id) is not None
