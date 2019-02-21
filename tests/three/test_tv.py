import pytest

from . import polite


tv_id = 1418  # The Big Bang Theory


@polite
def test_get_tv_details(tmdb):
    assert tmdb.get_tv_details(tv_id) is not None


@polite
def test_get_tv_account_states(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.get_tv_account_states(tv_id)


@polite
def test_get_tv_alternative_titles(tmdb):
    assert tmdb.get_tv_alternative_titles(tv_id) is not None


@polite
def test_get_tv_changes(tmdb):
    assert tmdb.get_tv_changes(tv_id) is not None


@polite
def test_get_tv_content_ratings(tmdb):
    assert tmdb.get_tv_content_ratings(tv_id) is not None


@polite
def test_get_tv_credits(tmdb):
    assert tmdb.get_tv_credits(tv_id) is not None


@polite
def test_get_tv_episode_groups(tmdb):
    assert tmdb.get_tv_episode_groups(tv_id) is not None


@polite
def test_get_tv_external_ids(tmdb):
    assert tmdb.get_tv_external_ids(tv_id) is not None


@polite
def test_get_tv_images(tmdb):
    assert tmdb.get_tv_images(tv_id) is not None


@polite
def test_get_tv_keywords(tmdb):
    assert tmdb.get_tv_keywords(tv_id) is not None


@polite
def test_get_tv_recommendations(tmdb):
    assert tmdb.get_tv_recommendations(tv_id) is not None


@polite
def test_get_tv_reviews(tmdb):
    assert tmdb.get_tv_reviews(tv_id) is not None


@polite
def test_get_tv_screened_theatrically(tmdb):
    assert tmdb.get_tv_screened_theatrically(tv_id) is not None


@polite
def test_get_tv_similar(tmdb):
    assert tmdb.get_tv_similar(tv_id) is not None


@polite
def test_get_tv_translations(tmdb):
    assert tmdb.get_tv_translations(tv_id) is not None


@polite
def test_get_tv_videos(tmdb):
    assert tmdb.get_tv_videos(tv_id) is not None


@polite
def test_post_tv_rating(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.post_tv_rating(tv_id, 10)


@polite
def test_delete_tv_rating(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.delete_tv_rating(tv_id)


@polite
def test_get_latest_tvs(tmdb):
    assert tmdb.get_latest_tvs() is not None


@polite
def test_get_tvs_airing_today(tmdb):
    assert tmdb.get_tvs_airing_today() is not None


@polite
def test_get_tvs_on_the_air(tmdb):
    assert tmdb.get_tvs_on_the_air() is not None


@polite
def test_get_popular_tvs(tmdb):
    assert tmdb.get_popular_tvs() is not None


@polite
def test_get_top_rated_tvs(tmdb):
    assert tmdb.get_top_rated_tvs() is not None
