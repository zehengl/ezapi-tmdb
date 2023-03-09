from .base import ENDPOINT, process_response


class TVEpisodeGroupsMixin:
    @process_response
    def get_tv_episode_group_details(self, tv_episode_group_id, **kwargs):
        """
        GET /tv/episode_group/{id}
        """

        url = f"{ENDPOINT}/3/tv/episode_group/{tv_episode_group_id}"
        return self.make_request("GET", url, kwargs)
