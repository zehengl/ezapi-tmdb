from .base import process_response, ENDPOINT, any_required_kwargs


class ListMixin:
    @process_response
    def get_list(self, list_id, **kwargs):
        """
        GET /list/{list_id}
        """

        url = f"{ENDPOINT}/4/list/{list_id}"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["media_type", "media_id"])
    @process_response
    def get_list_item_status(self, list_id, **kwargs):
        """
        GET /list/{list_id}/item_status
        """

        url = f"{ENDPOINT}/4/list/{list_id}/item_status"
        return self.make_request("GET", url, kwargs)
