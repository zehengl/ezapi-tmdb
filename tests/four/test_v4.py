import os

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
from dotenv import load_dotenv
from tmdb.four import TMDb

load_dotenv()


class TMDb4TestClass(BaseCase):
    def test_v4_api(self):
        access_token = os.getenv("access_token")
        username = os.getenv("username")
        password = os.getenv("password")

        msg = "Missing one or more configs (username, password, access_token)"
        if not all([username, password, access_token]):
            assert False, msg

        tmdb = TMDb(access_token)

        request_token = tmdb.create_request_token().get("request_token")

        self.open(
            f"https://www.themoviedb.org/auth/access?request_token={request_token}"
        )
        self.click_link("Login")
        self.type("username", username, By.ID)
        self.type("password", password, By.ID)
        self.click("login_button", by=By.ID)
        self.click('input[value="Approve"]')

        resp = tmdb.create_access_token(request_token)
        assert resp is not None

        user_access_token = resp.get("access_token")
        account_id = resp.get("account_id")

        tmdb.update_access_token(user_access_token)

        # /account
        assert tmdb.get_account_lists(account_id) is not None
        assert tmdb.get_account_favorite_movies(account_id) is not None
        assert tmdb.get_account_favorite_tv_shows(account_id) is not None

        # assert tmdb.get_account_movie_recommendations(account_id) is not None
        # assert tmdb.get_account_tv_show_recommendations(account_id) is not None

        assert tmdb.get_account_movie_watchlist(account_id) is not None
        assert tmdb.get_account_tv_show_watchlist(account_id) is not None
        assert tmdb.get_account_rated_movies(account_id) is not None
        assert tmdb.get_account_rated_tv_shows(account_id) is not None

        # /list
        assert tmdb.get_list(14105) is not None

        assert tmdb.get_list(14151) is not None

        assert (
            tmdb.get_list_item_status(
                14151,
                media_id=550,
                media_type="movie",
            )
            is not None
        )

        assert (
            tmdb.get_list_item_status(
                14105,
                media_id=1418,
                media_type="tv",
            )
            is not None
        )
