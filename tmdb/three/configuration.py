from .base import ENDPOINT, process_response


class ConfigurationMixin:
    @process_response
    def get_api_configuration(self, **kwargs):
        """
        GET /configuration
        """

        url = f"{ENDPOINT}/3/configuration"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_countries(self, **kwargs):
        """
        GET /configuration/countries
        """

        url = f"{ENDPOINT}/3/configuration/countries"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_jobs(self, **kwargs):
        """
        GET /configuration/jobs
        """

        url = f"{ENDPOINT}/3/configuration/jobs"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_languages(self, **kwargs):
        """
        GET /configuration/languages
        """

        url = f"{ENDPOINT}/3/configuration/languages"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_primary_translations(self, **kwargs):
        """
        GET /configuration/primary_translations
        """

        url = f"{ENDPOINT}/3/configuration/primary_translations"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_timezones(self, **kwargs):
        """
        GET /configuration/timezones
        """

        url = f"{ENDPOINT}/3/configuration/timezones"
        return self.make_request("GET", url, kwargs)
