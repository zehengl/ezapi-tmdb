import pytest

from . import polite


@polite
def test_get_tv_details(tmdb):
    assert tmdb.get_tv_details(1418) is not None


@polite
def test_get_tv_account_states(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.get_tv_account_states(1418)


@polite
def test_get_tv_alternative_titles(tmdb):
    assert tmdb.get_tv_alternative_titles(1418) is not None


@polite
def test_get_tv_changes(tmdb):
    assert tmdb.get_tv_changes(1418) is not None


@polite
def test_get_tv_content_ratings(tmdb):
    assert tmdb.get_tv_content_ratings(1418) is not None


@polite
def test_get_tv_credits(tmdb):
    assert tmdb.get_tv_credits(1418) is not None


@polite
def test_get_tv_episode_groups(tmdb):
    assert tmdb.get_tv_episode_groups(1418) is not None


@polite
def test_get_tv_external_ids(tmdb):
    assert tmdb.get_tv_external_ids(1418) is not None


@polite
def test_get_tv_images(tmdb):
    assert tmdb.get_tv_images(1418) is not None


@polite
def test_get_tv_keywords(tmdb):
    assert tmdb.get_tv_keywords(1418) is not None


@polite
def test_get_tv_recommendations(tmdb):
    assert tmdb.get_tv_recommendations(1418) is not None


@polite
def test_get_tv_reviews(tmdb):
    assert tmdb.get_tv_reviews(1418) is not None


@polite
def test_get_tv_screened_theatrically(tmdb):
    assert tmdb.get_tv_screened_theatrically(1418) is not None


@polite
def test_get_tv_similar(tmdb):
    assert tmdb.get_tv_similar(1418) is not None


@polite
def test_get_tv_translations(tmdb):
    assert tmdb.get_tv_translations(1418) is not None


@polite
def test_get_tv_videos(tmdb):
    assert tmdb.get_tv_videos(1418) is not None


@polite
def test_post_tv_rating(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.post_tv_rating(1418, 10)


@polite
def test_delete_tv_rating(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.delete_tv_rating(1418)


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
