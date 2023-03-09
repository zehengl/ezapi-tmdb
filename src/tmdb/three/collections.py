from .base import ENDPOINT, process_response


class CollectionsMixin:
    @process_response
    def get_collection_details(self, collection_id, **kwargs):
        """
        GET /collection/{collection_id}
        """

        url = f"{ENDPOINT}/3/collection/{collection_id}"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_collection_images(self, collection_id, **kwargs):
        """
        GET /collection/{collection_id}/images
        """

        url = f"{ENDPOINT}/3/collection/{collection_id}/images"
        return self.make_request("GET", url, kwargs)

    @process_response
    def get_collection_translations(self, collection_id, **kwargs):
        """
        GET /collection/{collection_id}/translations
        """

        url = f"{ENDPOINT}/3/collection/{collection_id}/translations"
        return self.make_request("GET", url, kwargs)
