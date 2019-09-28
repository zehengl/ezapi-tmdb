from .base import ENDPOINT, process_response


class CreditsMixin:
    @process_response
    def get_credit_details(self, credit_id, **kwargs):
        """
        GET /credit/{credit_id}
        """

        url = f"{ENDPOINT}/3/credit/{credit_id}"
        return self.make_request("GET", url, kwargs)
