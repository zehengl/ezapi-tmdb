from .base import ENDPOINT, process_response


class GenresMixin:
    @process_response
    def get_movie_genre_list(self, **kwargs):
        url = f"{ENDPOINT}/3/genre/movie/list"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_genre_list(self, **kwargs):
        url = f"{ENDPOINT}/3/genre/tv/list"
        return self.make_request("GET", url, kwargs)
