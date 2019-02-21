from .base import ENDPOINT, process_response


class GuestSessionsMixin:
    @process_response
    def get_guest_session_rated_movies(self, guest_session_id, **kwargs):
        url = f"{ENDPOINT}/3/guest_session/{guest_session_id}/rated/movies"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_guest_session_rated_tvs(self, guest_session_id, **kwargs):
        url = f"{ENDPOINT}/3/guest_session/{guest_session_id}/rated/tv"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_guest_session_rated_tv_episodes(self, guest_session_id, **kwargs):
        url = f"{ENDPOINT}/3/guest_session/{guest_session_id}/rated/tv/episodes"
        return self.make_request("GET", url, kwargs)
