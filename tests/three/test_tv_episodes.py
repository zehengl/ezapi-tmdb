import pytest
from utils import polite

tv_id = 1418  # The Big Bang Theory
season_number = 12
episode_number = 1


@polite
def test_get_tv_episode_details(tmdb):
    assert tmdb.get_tv_episode_details(tv_id, season_number, episode_number) is not None


@polite
def test_get_tv_episode_changes(tmdb):
    episode_id = tmdb.get_tv_episode_details(tv_id, season_number, episode_number).get(
        "id"
    )
    assert tmdb.get_tv_episode_changes(episode_id) is not None


@polite
@pytest.mark.parametrize("with_guest_session", [True, False])
def test_post_tv_episode_rating(tmdb, with_guest_session):
    rating = 10

    if with_guest_session:
        guest_session_id = tmdb.create_guest_session().get("guest_session_id")
        assert tmdb.post_tv_episode_rating(
            tv_id,
            season_number,
            episode_number,
            rating,
            guest_session_id=guest_session_id,
        )
    else:
        with pytest.raises(RuntimeError):
            assert tmdb.post_tv_episode_rating(
                tv_id, season_number, episode_number, rating
            )


@polite
@pytest.mark.parametrize("with_guest_session", [True, False])
def test_delete_tv_episode_rating(tmdb, with_guest_session):
    if with_guest_session:
        guest_session_id = tmdb.create_guest_session().get("guest_session_id")
        assert tmdb.delete_tv_episode_rating(
            tv_id, season_number, episode_number, guest_session_id=guest_session_id
        )
    else:
        with pytest.raises(RuntimeError):
            assert tmdb.delete_tv_episode_rating(tv_id, season_number, episode_number)


@polite
def test_get_tv_episode_credits(tmdb):
    assert tmdb.get_tv_episode_credits(tv_id, season_number, episode_number) is not None


@polite
def test_get_tv_episode_external_ids(tmdb):
    assert (
        tmdb.get_tv_episode_external_ids(tv_id, season_number, episode_number)
        is not None
    )


@polite
def test_get_tv_episode_images(tmdb):
    assert tmdb.get_tv_episode_images(tv_id, season_number, episode_number) is not None


@polite
def test_get_tv_episode_translations(tmdb):
    assert (
        tmdb.get_tv_episode_translations(tv_id, season_number, episode_number)
        is not None
    )


@polite
def test_get_tv_episode_videos(tmdb):
    assert tmdb.get_tv_episode_videos(tv_id, season_number, episode_number) is not None
