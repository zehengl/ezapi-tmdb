import requests

import tmdb

base_path = '/3'


class Endpoints:
    CERTIFICATIONS = '/certification/%s/list'
    CHANGES = '/%s/changes'
    COLLECTIONS = '/collection/%s'
    DISCOVER = '/discover/%s'
    GENRES = '/genre/%s/list'
    GENRE_MOVIES = '/genre/%d/movies'
    JOBS = '/job/list'
    SEARCH = '/search/%s'
    TIMEZONES = '/timezones/list'
    CONFIGURATION = '/configuration'


class TMDb:
    def __init__(self, api_key):
        self.api_key = api_key

    def _make_request(self, method, url, kwargs):
        kwargs['api_key'] = self.api_key
        return requests.request(method, url, params=kwargs).json()

    @staticmethod
    def _certifications_url(option):
        return '%s%s%s' % (
            tmdb.api.host,
            base_path,
            Endpoints.CERTIFICATIONS % option,
        )

    @staticmethod
    def _changes_url(option):
        return '%s%s%s' % (
            tmdb.api.host,
            base_path,
            Endpoints.CHANGES % option,
        )

    @staticmethod
    def _configuration():
        return '%s%s%s' % (
            tmdb.api.host,
            base_path,
            Endpoints.CONFIGURATION,
        )

    @staticmethod
    def _discover_url(option):
        return '%s%s%s' % (
            tmdb.api.host,
            base_path,
            Endpoints.DISCOVER % option
        )

    @staticmethod
    def _genres_url(option):
        return '%s%s%s' % (
            tmdb.api.host,
            base_path,
            Endpoints.GENRES % option,
        )

    @staticmethod
    def _genre_movies_url(genre_id):
        return '%s%s%s' % (
            tmdb.api.host,
            base_path,
            Endpoints.GENRE_MOVIES % genre_id,
        )

    @staticmethod
    def _jobs_url():
        return '%s%s%s' % (
            tmdb.api.host,
            base_path,
            Endpoints.JOBS
        )

    @staticmethod
    def _search_url(option):
        return '%s%s%s' % (
            tmdb.api.host,
            base_path,
            Endpoints.SEARCH % option,
        )

    @staticmethod
    def _timezones_url():
        return '%s%s%s' % (
            tmdb.api.host,
            base_path,
            Endpoints.TIMEZONES,
        )

    def certifications(self, option, **kwargs):
        return self._make_request(
            'GET',
            self._certifications_url(option),
            kwargs,
        )

    def changes(self, option, **kwargs):
        return self._make_request(
            'GET',
            self._changes_url(option),
            kwargs,
        )

    def configuration(self, **kwargs):
        return self._make_request(
            'GET',
            self._configuration(),
            kwargs,
        )

    def discover(self, option, **kwargs):
        return self._make_request(
            'GET',
            self._discover_url(option),
            kwargs,
        )

    def genres(self, option, **kwargs):
        return self._make_request(
            'GET',
            self._genres_url(option),
            kwargs,
        )

    def genre_movies(self, genre_id, **kwargs):
        return self._make_request(
            'GET',
            self._genre_movies_url(genre_id),
            kwargs,
        )

    def jobs(self, **kwargs):
        return self._make_request(
            'GET',
            self._jobs_url(),
            kwargs,
        )

    def search(self, option, **kwargs):
        return self._make_request(
            'GET',
            self._search_url(option),
            kwargs,
        )

    def timezones(self, **kwargs):
        return self._make_request(
            'GET',
            self._timezones_url(),
            kwargs,
        )
