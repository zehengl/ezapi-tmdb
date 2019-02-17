from .base import ENDPOINT, process_response


class CompaniesMixin:
    @process_response
    def get_company_details(self, company_id, **kwargs):
        url = f"{ENDPOINT}/3/company/{company_id}"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_company_alternative_names(self, company_id, **kwargs):
        url = f"{ENDPOINT}/3/company/{company_id}/alternative_names"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_company_images(self, company_id, **kwargs):
        url = f"{ENDPOINT}/3/company/{company_id}/images"
        return self.make_request("GET", url, kwargs)
