from .base import ENDPOINT, process_response


class AuthenticationMixin:
    @process_response
    def create_guest_session(self, **kwargs):
        url = f"{ENDPOINT}/3/authentication/guest_session/new"
        return self.make_request("GET", url, kwargs)
