from .base import ENDPOINT, any_required_kwargs, process_response


class TVEpisodesMixin:
    @process_response
    def get_tv_episode_details(self, tv_id, season_number, episode_number, **kwargs):
        """
        GET /tv/{tv_id}/season/{season_number}/episode/{episode_number}
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_episode_changes(self, episode_id, **kwargs):
        """
        GET /tv/episode/{episode_id}/changes
        """

        url = f"{ENDPOINT}/3/tv/episode/{episode_id}/changes"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_tv_episode_account_states(
        self, tv_id, season_number, episode_number, **kwargs
    ):
        """
        GET /tv/{tv_id}/season/{season_number}/episode/{episode_number}/account_states
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/account_states"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_episode_credits(self, tv_id, season_number, episode_number, **kwargs):
        """
        GET /tv/{tv_id}/season/{season_number}/episode/{episode_number}/credits
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/credits"
        return self.make_request("GET", url, kwargs)

    @process_response
    # fmt: off
    def get_tv_episode_external_ids(self, tv_id, season_number, episode_number, **kwargs):
    # fmt: on
        """
        GET /tv/{tv_id}/season/{season_number}/episode/{episode_number}/external_ids
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/external_ids"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_episode_images(self, tv_id, season_number, episode_number, **kwargs):
        """
        GET /tv/{tv_id}/season/{season_number}/episode/{episode_number}/images
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/images"
        return self.make_request("GET", url, kwargs)

    @process_response
    # fmt: off
    def get_tv_episode_translations(self, tv_id, season_number, episode_number, **kwargs):
    # fmt: on
        """
        GET /tv/{tv_id}/season/{season_number}/episode/{episode_number}/translations
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/translations"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"], ["guest_session_id"])
    @process_response
    # fmt: off
    def post_tv_episode_rating(self, tv_id, season_number, episode_number, rating, **kwargs):
    # fmt: on
        """
        POST /tv/{tv_id}/season/{season_number}/episode/{episode_number}/rating
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/rating"
        payload = {"value": rating}
        return self.make_request("POST", url, kwargs, payload)

    @any_required_kwargs(["session_id"], ["guest_session_id"])
    @process_response
    def delete_tv_episode_rating(self, tv_id, season_number, episode_number, **kwargs):
        """
        DELETE /tv/{tv_id}/season/{season_number}/episode/{episode_number}/rating
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/rating"
        return self.make_request("DELETE", url, kwargs)

    @process_response
    def get_tv_episode_videos(self, tv_id, season_number, episode_number, **kwargs):
        """
        GET /tv/{tv_id}/season/{season_number}/episode/{episode_number}/videos
        """

        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}/videos"
        return self.make_request("GET", url, kwargs)
