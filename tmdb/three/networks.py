from .base import ENDPOINT, process_response


class NetworksMixin:
    @process_response
    def get_network_details(self, network_id, **kwargs):
        url = f"{ENDPOINT}/3/network/{network_id}"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_network_alternative_names(self, network_id, **kwargs):
        url = f"{ENDPOINT}/3/network/{network_id}/alternative_names"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_network_images(self, network_id, **kwargs):
        url = f"{ENDPOINT}/3/network/{network_id}/images"
        return self.make_request("GET", url, kwargs)
