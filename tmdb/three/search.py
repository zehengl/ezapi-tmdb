from .base import ENDPOINT, any_required_kwargs, process_response


class SearchMixin:
    @any_required_kwargs(["query"])
    @process_response
    def get_company_search(self, **kwargs):
        """
        GET /search/company
        """

        url = f"{ENDPOINT}/3/search/company"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["query"])
    @process_response
    def get_collection_search(self, **kwargs):
        """
        GET /search/collection
        """

        url = f"{ENDPOINT}/3/search/collection"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["query"])
    @process_response
    def get_keyword_search(self, **kwargs):
        """
        GET /search/keyword
        """

        url = f"{ENDPOINT}/3/search/keyword"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["query"])
    @process_response
    def get_movie_search(self, **kwargs):
        """
        GET /search/movie
        """

        url = f"{ENDPOINT}/3/search/movie"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["query"])
    @process_response
    def get_multi_search(self, **kwargs):
        """
        GET /search/multi
        """

        url = f"{ENDPOINT}/3/search/multi"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["query"])
    @process_response
    def get_person_search(self, **kwargs):
        """
        GET /search/person
        """

        url = f"{ENDPOINT}/3/search/person"
        return self.make_request("GET", url, kwargs)

    @any_required_kwargs(["query"])
    @process_response
    def get_tv_search(self, **kwargs):
        """
        GET /search/tv
        """

        url = f"{ENDPOINT}/3/search/tv"
        return self.make_request("GET", url, kwargs)
