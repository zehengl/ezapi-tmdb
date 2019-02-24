from .base import ENDPOINT, any_required_kwargs, process_response


class AccountMixin:
    @any_required_kwargs(["session_id"])
    @process_response
    def get_account_details(self, **kwargs):
        url = f"{ENDPOINT}/3/account"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_account_lists(self, account_id, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/lists"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_account_favorite_movies(self, account_id, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/favorite/movies"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_account_favorite_tvs(self, account_id, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/favorite/tv"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def mark_as_favorite(self, account_id, media_type, media_id, favorite, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/favorite"
        payload = {
            "media_type": media_type,
            "media_id": media_id,
            "favorite": str(favorite).lower(),
        }
        return self.make_request("POST", url, kwargs, payload)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_account_rated_movies(self, account_id, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/rated/movies"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_account_rated_tvs(self, account_id, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/rated/tv"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_account_rated_tv_episodes(self, account_id, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/rated/tv/episodes"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_account_movie_watchlist(self, account_id, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/watchlist/movies"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_account_tv_watchlist(self, account_id, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/watchlist/tv"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def add_to_watchlist(self, account_id, media_type, media_id, watchlist, **kwargs):
        url = f"{ENDPOINT}/3/account/{account_id}/watchlist"
        payload = {
            "media_type": media_type,
            "media_id": media_id,
            "watchlist": str(watchlist).lower(),
        }
        return self.make_request("POST", url, kwargs, payload)
