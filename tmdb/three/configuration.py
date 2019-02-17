from .base import ENDPOINT, process_response


class ConfigurationMixin:
    @process_response
    def get_api_configuration(self, **kwargs):
        url = f"{ENDPOINT}/3/configuration"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_countries(self, **kwargs):
        url = f"{ENDPOINT}/3/configuration/countries"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_jobs(self, **kwargs):
        url = f"{ENDPOINT}/3/configuration/jobs"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_languages(self, **kwargs):
        url = f"{ENDPOINT}/3/configuration/languages"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_primary_translations(self, **kwargs):
        url = f"{ENDPOINT}/3/configuration/primary_translations"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_timezones(self, **kwargs):
        url = f"{ENDPOINT}/3/configuration/timezones"
        return self.make_request("GET", url, kwargs)
