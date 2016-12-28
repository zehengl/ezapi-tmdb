import unittest

from tests import credential_v3, is_error
from tmdb.api.v3 import TMDb


class TestTMDbV3(unittest.TestCase):

    def setUp(self):
        self.tmdb_obj = TMDb(
            credential_v3.get('api_key')
        )

    def testCertifications_valid(self):
        for option in ['movie', 'tv']:
            resp = self.tmdb_obj.certifications(option)
            self.assertFalse(is_error(resp))

    def testCertifications_invalid(self):
        resp = self.tmdb_obj.certifications('song')
        self.assertTrue(is_error(resp))

    def testChanges_valid(self):
        for option in ['movie', 'tv', 'person']:
            resp = self.tmdb_obj.changes(option)
            self.assertFalse(is_error(resp))

    def testChanges_invalid(self):
        resp = self.tmdb_obj.changes('song')
        self.assertTrue(is_error(resp))

    def testConfiguration(self):
        resp = self.tmdb_obj.configuration()
        self.assertFalse(is_error(resp))

    def testDiscover_valid(self):
        for option in ['movie', 'tv']:
            resp = self.tmdb_obj.discover(option)
            self.assertFalse(is_error(resp))

    def testDiscover_invalid(self):
        resp = self.tmdb_obj.discover('song')
        self.assertTrue(is_error(resp))

    def testGenres_valid(self):
        for option in ['movie', 'tv']:
            resp = self.tmdb_obj.genres(option)
            self.assertFalse(is_error(resp))

    def testGenres_invalid(self):
        resp = self.tmdb_obj.genres('song')
        self.assertTrue(is_error(resp))

    def testGenreMovies_valid(self):
        genres = self.tmdb_obj.genres('movie')
        for item in genres.get('genres'):
            resp = self.tmdb_obj.genre_movies(item.get('id'))
            self.assertFalse(is_error(resp))

    def testGenreMovies_invalid(self):
        resp = self.tmdb_obj.genre_movies(0)
        self.assertTrue(is_error(resp))

    def testJobs(self):
        resp = self.tmdb_obj.jobs()
        self.assertFalse(is_error(resp))

    def testSearch_valid(self):
        for option in ['company', 'collection', 'keyword', 'movie', 'multi', 'person', 'tv']:
            resp = self.tmdb_obj.search(option, query='star wars')
            self.assertFalse((is_error(resp)))

    def testSearch_invalid(self):
        resp = self.tmdb_obj.search('song', query='star wars')
        self.assertTrue(is_error(resp))

    def testTimezones(self):
        resp = self.tmdb_obj.timezones()
        self.assertFalse(is_error(resp))
