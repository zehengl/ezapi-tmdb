from .base import process_response, ENDPOINT


class AccountMixin:
    @process_response
    def get_account_lists(self, account_id, **kwargs):
        """
        GET /account/{account_id}/lists
        """

        url = f"{ENDPOINT}/4/account/{account_id}/lists"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_account_favorite_movies(self, account_id, **kwargs):
        """
        GET /account/{account_id}/movie/favorites
        """

        url = f"{ENDPOINT}/4/account/{account_id}/movie/favorites"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_account_favorite_tv_shows(self, account_id, **kwargs):
        """
        GET /account/{account_id}/tv/favorites
        """

        url = f"{ENDPOINT}/4/account/{account_id}/tv/favorites"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_account_movie_recommendations(self, account_id, **kwargs):
        """
        GET /account/{account_id}/movie/recommendations
        """

        url = f"{ENDPOINT}/4/account/{account_id}/movie/recommendations"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_account_tv_show_recommendations(self, account_id, **kwargs):
        """
        GET /account/{account_id}/tv/recommendations
        """

        url = f"{ENDPOINT}/4/account/{account_id}/tv/recommendations"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_account_movie_watchlist(self, account_id, **kwargs):
        """
        GET /account/{account_id}/movie/watchlist
        """

        url = f"{ENDPOINT}/4/account/{account_id}/movie/watchlist"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_account_tv_show_watchlist(self, account_id, **kwargs):
        """
        GET /account/{account_id}/tv/watchlist
        """

        url = f"{ENDPOINT}/4/account/{account_id}/tv/watchlist"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_account_rated_movies(self, account_id, **kwargs):
        """
        GET /account/{account_id}/movie/rated
        """

        url = f"{ENDPOINT}/4/account/{account_id}/movie/rated"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_account_rated_tv_shows(self, account_id, **kwargs):
        """
        GET /account/{account_id}/tv/rated
        """

        url = f"{ENDPOINT}/4/account/{account_id}/tv/rated"
        return self.make_request("GET", url, kwargs)
