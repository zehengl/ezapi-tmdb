import pytest


def test_get_movie_details(tmdb):
    assert tmdb.get_movie_details(597) is not None


def test_get_movie_account_states(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.get_movie_account_states(597)


def test_get_movie_alternative_titles(tmdb):
    assert tmdb.get_movie_alternative_titles(597) is not None


def test_get_movie_credits(tmdb):
    assert tmdb.get_movie_credits(597) is not None


def test_get_movie_changes(tmdb):
    assert tmdb.get_movie_changes(597) is not None


def test_get_movie_external_ids(tmdb):
    assert tmdb.get_movie_external_ids(597) is not None


def test_get_movie_images(tmdb):
    assert tmdb.get_movie_images(597) is not None


def test_get_movie_keywords(tmdb):
    assert tmdb.get_movie_keywords(597) is not None


def test_get_movie_release_dates(tmdb):
    assert tmdb.get_movie_release_dates(597) is not None


def test_get_movie_videos(tmdb):
    assert tmdb.get_movie_videos(597) is not None


def test_get_movie_translations(tmdb):
    assert tmdb.get_movie_translations(597) is not None


def test_get_movie_recommendations(tmdb):
    assert tmdb.get_movie_recommendations(597) is not None


def test_get_movie_similar(tmdb):
    assert tmdb.get_movie_similar(597) is not None


def test_get_movie_reviews(tmdb):
    assert tmdb.get_movie_reviews(597) is not None


def test_get_movie_lists(tmdb):
    assert tmdb.get_movie_lists(597) is not None


def test_post_movie_rating(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.post_movie_rating(597, 10)


def test_delete_movie_rating(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.delete_movie_rating(597)


def test_get_latest_movies(tmdb):
    assert tmdb.get_latest_movies() is not None


def test_get_now_playing_movies(tmdb):
    assert tmdb.get_now_playing_movies() is not None


def test_get_popular_movies(tmdb):
    assert tmdb.get_popular_movies() is not None


def test_get_top_rated_movies(tmdb):
    assert tmdb.get_top_rated_movies() is not None


def test_get_upcoming_movies(tmdb):
    assert tmdb.get_upcoming_movies() is not None
