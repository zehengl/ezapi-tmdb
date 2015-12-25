ezapi\_tmdb
===========

An easy api for TMDb written in Python

It implements the api provided by TMDb. For details, see
http://docs.themoviedb.apiary.io/#

Install
=======

.. code:: bash

    pip install ezapi_tmdb

Usage
=====

.. code:: python

    from ezapi_yelp import EZapiTMDb

    api_key = 'YOUR api_key'
    test_api = EZapiTMDb(api_key)

    # Simple examples

    print test_api.configuration()

    for t in test_api.category_certifications:
        print test_api.certifications(t)

    for t in test_api.category_changes:
        print test_api.changes(t)

    for t in test_api.category_discover:
        print test_api.discover(t)

    for t in test_api.category_genres:
        print test_api.genres(t)

    print test_api.jobs()

    print test_api.timezones()

    print test_api.search('movie',query='star war')

    print test_api.search('person',query='matt damon')

    print test_api.search('tv',query='big bang')

    print test_api.detail('tv',1418)

    print test_api.detail('tv',1418,'credits')

Changelist
==========

-  2015/12/24

   -  Multiple "GET" api: configuration, certifications, changes,
      discover, genres, jobs, timezones
   -  Also the search api

      -  category: **company**, **collection**, **keyword**, **list**,
         **movie**, **multi**, **person**, **tv**
      -  api usage: .search(\ *category*, query="some key words")

   -  And detail for a search result, such as:

      -  /tv/**id** and /tv/**id**/changes
      -  /person/**id** and /person/**id**/tv\_credits

TODO
====

-  api that requires session\_id
-  unit tests
