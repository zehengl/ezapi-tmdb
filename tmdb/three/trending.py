from .base import ENDPOINT, process_response


class TrendingMixin:
    @process_response
    def get_trending(self, media_type, time_window, **kwargs):
        """
        GET /trending/{media_type}/{time_window}
        """

        url = f"{ENDPOINT}/3/trending/{media_type}/{time_window}"
        return self.make_request("GET", url, kwargs)
