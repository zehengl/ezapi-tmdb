from .base import ENDPOINT, any_required_kwargs, process_response


class ListsMixin:
    @process_response
    def get_list_details(self, list_id, **kwargs):
        """
        GET /list/{list_id}
        """

        url = f"{ENDPOINT}/3/list/{list_id}"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["movie_id"])
    @process_response
    def get_list_item_status(self, list_id, **kwargs):
        """
        GET /list/{list_id}/item_status
        """

        url = f"{ENDPOINT}/3/list/{list_id}/item_status"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def create_list(self, name, description="", language="", **kwargs):
        """
        POST /list
        """

        url = f"{ENDPOINT}/3/list"
        payload = {"name": name, "description": description, "language": language}
        return self.make_request("POST", url, kwargs, payload)

    @any_required_kwargs(["session_id"])
    @process_response
    def add_movie(self, list_id, media_id, **kwargs):
        """
        POST /list/{list_id}/add_item
        """

        url = f"{ENDPOINT}/3/list/{list_id}/add_item"
        payload = {"media_id": media_id}
        return self.make_request("POST", url, kwargs, payload)

    @any_required_kwargs(["session_id"])
    @process_response
    def remove_movie(self, list_id, media_id, **kwargs):
        """
        POST /list/{list_id}/remove_item
        """

        url = f"{ENDPOINT}/3/list/{list_id}/remove_item"
        payload = {"media_id": media_id}
        return self.make_request("POST", url, kwargs, payload)

    @any_required_kwargs(["session_id", "confirm"])
    @process_response
    def clear_list(self, list_id, **kwargs):
        """
        POST /list/{list_id}/clear
        """

        kwargs["confirm"] = str(kwargs["confirm"]).lower()
        url = f"{ENDPOINT}/3/list/{list_id}/clear"
        return self.make_request("POST", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def delete_list(self, list_id, **kwargs):
        """
        DELETE /list/{list_id}
        """

        url = f"{ENDPOINT}/3/list/{list_id}"
        return self.make_request("DELETE", url, kwargs)
