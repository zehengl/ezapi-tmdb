from .base import process_response, ENDPOINT


class ListMixin:
    @process_response
    def get_list(self, list_id, **kwargs):
        """
        GET /list/{list_id}
        """

        url = f"{ENDPOINT}/4/list/{list_id}"
        return self.make_request("GET", url, kwargs)
