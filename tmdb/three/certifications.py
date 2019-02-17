from .base import ENDPOINT, process_response


class CertificationsMixin:
    @process_response
    def get_movie_certifications(self, **kwargs):
        url = f"{ENDPOINT}/3/certification/movie/list"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_tv_certifications(self, **kwargs):
        url = f"{ENDPOINT}/3/certification/tv/list"
        return self.make_request("GET", url, kwargs)
