from .base import ENDPOINT, process_response


class PeopleMixin:
    @process_response
    def get_person_details(self, person_id, **kwargs):
        """
        GET /person/{person_id}
        """

        url = f"{ENDPOINT}/3/person/{person_id}"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_person_changes(self, person_id, **kwargs):
        """
        GET /person/{person_id}/changes
        """

        url = f"{ENDPOINT}/3/person/{person_id}/changes"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_person_movie_credits(self, person_id, **kwargs):
        """
        GET /person/{person_id}/movie_credits
        """

        url = f"{ENDPOINT}/3/person/{person_id}/movie_credits"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_person_tv_credits(self, person_id, **kwargs):
        """
        GET /person/{person_id}/tv_credits
        """

        url = f"{ENDPOINT}/3/person/{person_id}/tv_credits"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_person_combined_credits(self, person_id, **kwargs):
        """
        GET /person/{person_id}/combined_credits
        """

        url = f"{ENDPOINT}/3/person/{person_id}/combined_credits"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_person_external_ids(self, person_id, **kwargs):
        """
        GET /person/{person_id}/external_ids
        """

        url = f"{ENDPOINT}/3/person/{person_id}/external_ids"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_person_images(self, person_id, **kwargs):
        """
        GET /person/{person_id}/images
        """

        url = f"{ENDPOINT}/3/person/{person_id}/images"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_person_tagged_images(self, person_id, **kwargs):
        """
        GET /person/{person_id}/tagged_images
        """

        url = f"{ENDPOINT}/3/person/{person_id}/tagged_images"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_person_translations(self, person_id, **kwargs):
        """
        GET /person/{person_id}/translations
        """

        url = f"{ENDPOINT}/3/person/{person_id}/translations"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_latest_person(self, **kwargs):
        """
        GET /person/latest
        """

        url = f"{ENDPOINT}/3/person/latest"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_popular_persons(self, **kwargs):
        """
        GET /person/popular
        """

        url = f"{ENDPOINT}/3/person/popular"
        return self.make_request("GET", url, kwargs)
