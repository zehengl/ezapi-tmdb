from .base import ENDPOINT, any_required_kwargs, process_response


class TVSeasonsMixin:
    @process_response
    def get_tv_season_details(self, tv_id, season_number, **kwargs):
        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["session_id"])
    @process_response
    def get_tv_season_account_states(self, tv_id, season_number, **kwargs):
        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/account_states"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_season_changes(self, season_number, **kwargs):
        url = f"{ENDPOINT}/3/tv/season/{season_number}/changes"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_season_credits(self, tv_id, season_number, **kwargs):
        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/credits"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_season_external_ids(self, tv_id, season_number, **kwargs):
        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/external_ids"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_season_images(self, tv_id, season_number, **kwargs):
        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/images"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_season_videos(self, tv_id, season_number, **kwargs):
        url = f"{ENDPOINT}/3/tv/{tv_id}/season/{season_number}/videos"
        return self.make_request("GET", url, kwargs)
