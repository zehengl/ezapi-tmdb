from .base import ENDPOINT, any_required_kwargs, process_response


class MoviesMixin:
    @process_response
    def get_movie_details(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_movie_account_states(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/account_states"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_alternative_titles(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/alternative_titles"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_changes(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/changes"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_credits(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/credits"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_external_ids(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/external_ids"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_images(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/images"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_keywords(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/keywords"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_release_dates(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/release_dates"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_videos(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/videos"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_translations(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/translations"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_recommendations(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/recommendations"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_similar(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/similar"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_reviews(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/reviews"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_movie_lists(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/lists"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"], ["guest_session_id"])
    @process_response
    def post_movie_rating(self, movie_id, payload, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/rating"
        return self.make_request("POST", url, kwargs, payload)

    @any_required_kwargs(["session_id"], ["guest_session_id"])
    @process_response
    def delete_movie_rating(self, movie_id, **kwargs):
        url = f"{ENDPOINT}/3/movie/{movie_id}/rating"
        return self.make_request("DELETE", url, kwargs)

    @process_response
    def get_latest_movies(self, **kwargs):
        url = f"{ENDPOINT}/3/movie/latest"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_now_playing_movies(self, **kwargs):
        url = f"{ENDPOINT}/3/movie/now_playing"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_popular_movies(self, **kwargs):
        url = f"{ENDPOINT}/3/movie/popular"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_top_rated_movies(self, **kwargs):
        url = f"{ENDPOINT}/3/movie/top_rated"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_upcoming_movies(self, **kwargs):
        url = f"{ENDPOINT}/3/movie/upcoming"
        return self.make_request("GET", url, kwargs)
