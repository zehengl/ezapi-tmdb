from .base import ENDPOINT, any_required_kwargs, process_response


class TVsMixin:
    @process_response
    def get_tv_details(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_tv_account_states(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/account_states
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/account_states"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_alternative_titles(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/alternative_titles
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/alternative_titles"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_changes(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/changes
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/changes"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_content_ratings(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/content_ratings
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/content_ratings"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_credits(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/credits
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/credits"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_episode_groups(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/episode_groups
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/episode_groups"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_external_ids(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/external_ids
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/external_ids"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_images(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/images
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/images"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_keywords(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/keywords
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/keywords"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_recommendations(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/recommendations
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/recommendations"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_reviews(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/reviews
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/reviews"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_screened_theatrically(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/screened_theatrically
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/screened_theatrically"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_similar(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/similar
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/similar"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_translations(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/translations
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/translations"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_videos(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/videos
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/videos"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_watch_providers(self, tv_id, **kwargs):
        """
        GET /tv/{tv_id}/watch/providers
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/watch/providers"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"], ["guest_session_id"])
    @process_response
    def post_tv_rating(self, tv_id, rating, **kwargs):
        """
        POST /tv/{tv_id}/rating
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/rating"
        payload = {"value": rating}
        return self.make_request("POST", url, kwargs, payload)

    @any_required_kwargs(["session_id"], ["guest_session_id"])
    @process_response
    def delete_tv_rating(self, tv_id, **kwargs):
        """
        DELETE /tv/{tv_id}/rating
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/rating"
        return self.make_request("DELETE", url, kwargs)

    @process_response
    def get_latest_tvs(self, **kwargs):
        """
        GET /tv/latest
        """

        url = f"{ENDPOINT}/3/tv/latest"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tvs_airing_today(self, **kwargs):
        """
        GET /tv/airing_today
        """

        url = f"{ENDPOINT}/3/tv/airing_today"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tvs_on_the_air(self, **kwargs):
        """
        GET /tv/on_the_air
        """

        url = f"{ENDPOINT}/3/tv/on_the_air"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_popular_tvs(self, **kwargs):
        """
        GET /tv/popular
        """

        url = f"{ENDPOINT}/3/tv/popular"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_top_rated_tvs(self, **kwargs):
        """
        GET /tv/top_rated
        """

        url = f"{ENDPOINT}/3/tv/top_rated"
        return self.make_request("GET", url, kwargs)
