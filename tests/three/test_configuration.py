from . import polite


@polite
def test_get_api_configuration(tmdb):
    assert tmdb.get_api_configuration() is not None


@polite
def test_get_countries(tmdb):
    assert tmdb.get_countries() is not None


@polite
def test_get_jobs(tmdb):
    assert tmdb.get_jobs() is not None


@polite
def test_get_languages(tmdb):
    assert tmdb.get_languages() is not None


@polite
def test_get_primary_translations(tmdb):
    assert tmdb.get_primary_translations() is not None


@polite
def test_get_timezones(tmdb):
    assert tmdb.get_timezones() is not None
