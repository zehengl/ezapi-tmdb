from .base import ENDPOINT, any_required_kwargs, process_response


class FindMixin:
    @any_required_kwargs(["external_source"])
    @process_response
    def find_by_id(self, external_id, **kwargs):
        url = f"{ENDPOINT}/3/find/{external_id}"
        return self.make_request("GET", url, kwargs)
