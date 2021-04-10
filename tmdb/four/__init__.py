import requests

from .account import AccountMixin
from .auth import AuthMixin
from .list import ListMixin

mixins = [
    AccountMixin,
    AuthMixin,
    ListMixin,
]


class TMDb(*mixins):
    def __init__(self, access_token, **kwargs):
        self.access_token = access_token
        self.options = kwargs
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": f"Bearer {access_token}",
            }
        )

    def make_request(self, method, url, request_params, payload=None):
        params = {}
        params.update(self.options)
        params.update(request_params)

        # https://developers.themoviedb.org/3/getting-started/image-languages
        # convert keyword argument: (..., include_image_language=["en", "null"])
        # into url param: ...&include_image_language=en,null
        for key in params:
            if type(params[key]) is list:
                params[key] = ",".join(params[key])

        return self.session.request(
            method, url, params=params, json=payload, timeout=30
        )

    def set_options(self, **kwargs):
        self.options.update(kwargs)

    def reset_options(self):
        self.options = {}

    def update_access_token(self, access_token):
        self.access_token = access_token
