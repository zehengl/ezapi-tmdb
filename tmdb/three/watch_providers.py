from .base import ENDPOINT, process_response


class WatchProvidersMixin:
    @process_response
    def get_available_regions(self, **kwargs):
        """
        GET /watch/providers/regions
        """

        url = f"{ENDPOINT}/3/watch/providers/regions"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_providers(self, **kwargs):
        """
        GET /watch/providers/movie
        """

        url = f"{ENDPOINT}/3/watch/providers/movie"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_providers(self, **kwargs):
        """
        GET /watch/providers/tv
        """

        url = f"{ENDPOINT}/3/watch/providers/tv"
        return self.make_request("GET", url, kwargs)
