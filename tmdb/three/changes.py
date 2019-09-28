from .base import ENDPOINT, process_response


class ChangesMixin:
    @process_response
    def get_movie_change_list(self, **kwargs):
        """
        GET /movie/changes
        """

        url = f"{ENDPOINT}/3/movie/changes"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_change_list(self, **kwargs):
        """
        GET /tv/changes
        """

        url = f"{ENDPOINT}/3/tv/changes"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_person_change_list(self, **kwargs):
        """
        GET /person/changes
        """

        url = f"{ENDPOINT}/3/person/changes"
        return self.make_request("GET", url, kwargs)
