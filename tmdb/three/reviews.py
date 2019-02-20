from .base import ENDPOINT, process_response


class ReviewsMixin:
    @process_response
    def get_review_details(self, review_id, **kwargs):
        url = f"{ENDPOINT}/3/review/{review_id}"
        return self.make_request("GET", url, kwargs)
