from .base import ENDPOINT, process_response


class AuthenticationMixin:
    @process_response
    def create_guest_session(self, **kwargs):
        url = f"{ENDPOINT}/3/authentication/guest_session/new"
        return self.make_request("GET", url, kwargs)

    @process_response
    def create_request_token(self, **kwargs):
        url = f"{ENDPOINT}/3/authentication/token/new"
        return self.make_request("GET", url, kwargs)

    @process_response
    def create_session(self, request_token, **kwargs):
        url = f"{ENDPOINT}/3/authentication/session/new"
        payload = {"request_token": request_token}
        return self.make_request("POST", url, kwargs, payload)

    @process_response
    def create_session_with_login(self, username, password, request_token, **kwargs):
        url = f"{ENDPOINT}/3/authentication/token/validate_with_login"
        payload = {
            "username": username,
            "password": password,
            "request_token": request_token,
        }
        return self.make_request("POST", url, kwargs, payload)

    @process_response
    def delete_session(self, session_id, **kwargs):
        url = f"{ENDPOINT}/3/authentication/session"
        payload = {"session_id": session_id}
        return self.make_request("DELETE", url, kwargs, payload)
