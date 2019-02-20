from .base import ENDPOINT, process_response


class KeywordsMixin:
    @process_response
    def get_keyword_details(self, keyword_id, **kwargs):
        url = f"{ENDPOINT}/3/keyword/{keyword_id}"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_keyword_movies(self, keyword_id, **kwargs):
        url = f"{ENDPOINT}/3/keyword/{keyword_id}/movies"
        return self.make_request("GET", url, kwargs)
