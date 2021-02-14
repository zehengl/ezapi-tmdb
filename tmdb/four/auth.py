from .base import process_response, ENDPOINT


class AuthMixin:
    @process_response
    def create_request_token(self, redirect_to="http://www.themoviedb.org/"):
        """
        POST /auth/request_token
        """

        url = f"{ENDPOINT}/4/auth/request_token"
        payload = {
            "redirect_to": redirect_to,
        }
        return self.make_request("POST", url, {}, payload)

    @process_response
    def create_access_token(self, request_token):
        """
        POST /auth/access_token
        """

        url = f"{ENDPOINT}/4/auth/access_token"
        payload = {
            "request_token": request_token,
        }
        return self.make_request("POST", url, {}, payload)
