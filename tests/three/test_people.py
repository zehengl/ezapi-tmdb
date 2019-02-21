from . import polite

person_id = 192  # Morgan Freeman


@polite
def test_get_person_details(tmdb):
    assert tmdb.get_person_details(person_id) is not None


@polite
def test_get_person_changes(tmdb):
    assert tmdb.get_person_changes(person_id) is not None


@polite
def test_get_person_movie_credits(tmdb):
    assert tmdb.get_person_movie_credits(person_id) is not None


@polite
def test_get_person_tv_credits(tmdb):
    assert tmdb.get_person_tv_credits(person_id) is not None


@polite
def test_get_person_combined_credits(tmdb):
    assert tmdb.get_person_combined_credits(person_id) is not None


@polite
def test_get_person_external_ids(tmdb):
    assert tmdb.get_person_external_ids(person_id) is not None


@polite
def test_get_person_images(tmdb):
    assert tmdb.get_person_images(person_id) is not None


@polite
def test_get_person_tagged_images(tmdb):
    assert tmdb.get_person_tagged_images(person_id) is not None


@polite
def test_get_person_translations(tmdb):
    assert tmdb.get_person_translations(person_id) is not None


@polite
def test_get_latest_person(tmdb):
    assert tmdb.get_latest_person() is not None


@polite
def test_get_popular_persons(tmdb):
    assert tmdb.get_popular_persons() is not None
