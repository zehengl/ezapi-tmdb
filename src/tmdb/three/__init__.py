import requests

from .account import AccountMixin
from .authentication import AuthenticationMixin
from .certifications import CertificationsMixin
from .changes import ChangesMixin
from .collections import CollectionsMixin
from .companies import CompaniesMixin
from .configuration import ConfigurationMixin
from .credits import CreditsMixin
from .discover import DiscoverMixin
from .find import FindMixin
from .genres import GenresMixin
from .guest_sessions import GuestSessionsMixin
from .keywords import KeywordsMixin
from .lists import ListsMixin
from .movies import MoviesMixin
from .networks import NetworksMixin
from .people import PeopleMixin
from .search import SearchMixin
from .reviews import ReviewsMixin
from .trending import TrendingMixin
from .tv import TVsMixin
from .tv_episodes import TVEpisodesMixin
from .tv_episode_groups import TVEpisodeGroupsMixin
from .tv_seasons import TVSeasonsMixin
from .watch_providers import WatchProvidersMixin

mixins = [
    AccountMixin,
    AuthenticationMixin,
    CertificationsMixin,
    ChangesMixin,
    CollectionsMixin,
    CompaniesMixin,
    ConfigurationMixin,
    CreditsMixin,
    DiscoverMixin,
    FindMixin,
    GenresMixin,
    GuestSessionsMixin,
    KeywordsMixin,
    ListsMixin,
    MoviesMixin,
    NetworksMixin,
    PeopleMixin,
    ReviewsMixin,
    SearchMixin,
    TrendingMixin,
    TVEpisodeGroupsMixin,
    TVEpisodesMixin,
    TVSeasonsMixin,
    TVsMixin,
    WatchProvidersMixin,
]


class TMDb(*mixins):
    def __init__(self, api_key, **kwargs):
        self.api_key = api_key
        self.options = kwargs
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json;charset=utf-8"})

    def make_request(self, method, url, request_params, payload=None):
        params = {"api_key": self.api_key}
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
