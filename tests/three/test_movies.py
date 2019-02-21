import pytest

from . import polite

movie_id = 597  # Titanic


@polite
def test_get_movie_details(tmdb):
    assert tmdb.get_movie_details(movie_id) is not None


@polite
def test_get_movie_account_states(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.get_movie_account_states(movie_id)


@polite
def test_get_movie_alternative_titles(tmdb):
    assert tmdb.get_movie_alternative_titles(movie_id) is not None


@polite
def test_get_movie_credits(tmdb):
    assert tmdb.get_movie_credits(movie_id) is not None


@polite
def test_get_movie_changes(tmdb):
    assert tmdb.get_movie_changes(movie_id) is not None


@polite
def test_get_movie_external_ids(tmdb):
    assert tmdb.get_movie_external_ids(movie_id) is not None


@polite
def test_get_movie_images(tmdb):
    assert tmdb.get_movie_images(movie_id) is not None


@polite
def test_get_movie_keywords(tmdb):
    assert tmdb.get_movie_keywords(movie_id) is not None


@polite
def test_get_movie_release_dates(tmdb):
    assert tmdb.get_movie_release_dates(movie_id) is not None


@polite
def test_get_movie_videos(tmdb):
    assert tmdb.get_movie_videos(movie_id) is not None


@polite
def test_get_movie_translations(tmdb):
    assert tmdb.get_movie_translations(movie_id) is not None


@polite
def test_get_movie_recommendations(tmdb):
    assert tmdb.get_movie_recommendations(movie_id) is not None


@polite
def test_get_movie_similar(tmdb):
    assert tmdb.get_movie_similar(movie_id) is not None


@polite
def test_get_movie_reviews(tmdb):
    assert tmdb.get_movie_reviews(movie_id) is not None


@polite
def test_get_movie_lists(tmdb):
    assert tmdb.get_movie_lists(movie_id) is not None


@polite
def test_post_movie_rating(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.post_movie_rating(movie_id, 10)


@polite
def test_delete_movie_rating(tmdb):
    with pytest.raises(RuntimeError):
        assert tmdb.delete_movie_rating(movie_id)


@polite
def test_get_latest_movies(tmdb):
    assert tmdb.get_latest_movies() is not None


@polite
def test_get_now_playing_movies(tmdb):
    assert tmdb.get_now_playing_movies() is not None


@polite
def test_get_popular_movies(tmdb):
    assert tmdb.get_popular_movies() is not None


@polite
def test_get_top_rated_movies(tmdb):
    assert tmdb.get_top_rated_movies() is not None


@polite
def test_get_upcoming_movies(tmdb):
    assert tmdb.get_upcoming_movies() is not None
