from .base import ENDPOINT, process_response


class DiscoverMixin:
    @process_response
    def get_movie_discover(self, **kwargs):
        url = f"{ENDPOINT}/3/discover/movie"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_discover(self, **kwargs):
        url = f"{ENDPOINT}/3/discover/tv"
        return self.make_request("GET", url, kwargs)
