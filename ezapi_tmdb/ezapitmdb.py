import requests


class EZapiTMDb:

    # Simple error that prints predefined message
    class EZerror(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    # requires api_key
    def __init__(self, api_key):
        # TMDb V3 api
        self.apiv3 = 'https://api.themoviedb.org/3/'
        self.category_search = ['company', 'collection', 'keyword', 'list', 'movie', 'multi', 'person', 'tv']
        self.category_certifications = ['movie', 'tv']
        self.category_discover = ['movie', 'tv']
        self.category_changes = ['movie', 'tv', 'person']
        self.category_genres = ['movie', 'tv']
        self.api_key = api_key

    def return_response(self, r):
        if r.status_code == 200:
            return r.json()
        else:
            raise EZapiTMDb.EZerror(r.json()['status_message'])

    # /configuration
    def configuration(self):
        r = requests.get(self.apiv3+'configuration', params={'api_key': self.api_key})
        return self.return_response(r)

    # /certification/{{category}}/list
    def certifications(self, category):
        if category not in self.category_certifications:
            raise EZapiTMDb.EZerror('Invalid certification category')
        r = requests.get(self.apiv3+'certification/'+category+'/list', params={'api_key': self.api_key})
        return self.return_response(r)

    # /{{category}}/changes
    def changes(self, category):
        if category not in self.category_changes:
            raise EZapiTMDb.EZerror('Invalid change category')
        r = requests.get(self.apiv3+category+'/changes', params={'api_key': self.api_key})
        return self.return_response(r)

    # /discover/{{category}}
    def discover(self, category):
        if category not in self.category_discover:
            raise EZapiTMDb.EZerror('Invalid discover category')
        r = requests.get(self.apiv3+'discover/'+category, params={'api_key': self.api_key})
        return self.return_response(r)

    # /genre/{{category}}/list
    def genres(self, category):
        if category not in self.category_genres:
            raise EZapiTMDb.EZerror('Invalid genre category')
        r = requests.get(self.apiv3+'genre/'+category+'/list', params={'api_key': self.api_key})
        return self.return_response(r)

    # /job/list
    def jobs(self):
        r = requests.get(self.apiv3+'job/list', params={'api_key': self.api_key})
        return self.return_response(r)

    # /timezones/list
    def timezones(self):
        r = requests.get(self.apiv3+'timezones/list', params={'api_key': self.api_key})
        return self.return_response(r)

    # /search/{{category}}
    def search(self, category, **kwargs):
        if category not in self.category_search:
            raise EZapiTMDb.EZerror('Invalid search category')
        kwargs['api_key'] = self.api_key
        r = requests.get(self.apiv3+'search/'+category, params=kwargs)
        return self.return_response(r)

    # {{category}}/id
    # {{category}}/id/opt
    # opt depends on {{category}}, e.g., /tv/similar
    def detail(self, category, id, opt=None, **kwargs):
        if isinstance(id, int):
            id = str(id)
        kwargs['api_key'] = self.api_key
        if opt:
            r = requests.get(self.apiv3+category+'/'+id+'/'+opt, params=kwargs)
        else:
            r = requests.get(self.apiv3+category+'/'+id, params=kwargs)
        return self.return_response(r)

