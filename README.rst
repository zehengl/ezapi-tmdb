ezapi-tmdb
==========

A Python wrapper for TMDb API, supporting version
`3 <https://developers.themoviedb.org/3/getting-started>`__

|Travis|\ |PyPI|\ |Coveralls|\ |Code Climate|

-  Implement all endpoints
-  Provide CLI
-  Include unit tests

Install
=======

.. code:: bash

    pip install ezapi_tmdb

Test
====

1. Clone down the repo

   .. code:: bash

       git clone git@github.com:zehengl/ezapi-tmdb.git
       cd ezapi-tmdb

2. Create a config file to store your api key for testing

   .. code:: bash

       touch tests/credentials.conf

3. Put donw your api key as follows

   ::

       [v3]
       api_key = xxxx

       [v4]
       api_key = xxxx

4. Run the tests

   .. code:: bash

       python setup.py test

Contact
=======

Zeheng Li

imzehengl@gmail.com

.. |Travis| image:: https://img.shields.io/travis/zehengl/ezapi-tmdb.svg
   :target: https://travis-ci.org/zehengl/ezapi-tmdb
.. |PyPI| image:: https://img.shields.io/pypi/v/ezapi-tmdb.svg
   :target: https://pypi.python.org/pypi/ezapi-tmdb
.. |Coveralls| image:: https://img.shields.io/coveralls/zehengl/ezapi-tmdb.svg
   :target: https://coveralls.io/github/zehengl/ezapi-tmdb
.. |Code Climate| image:: https://img.shields.io/codeclimate/github/zehengl/ezapi-tmdb.svg
   :target: https://codeclimate.com/github/zehengl/ezapi-tmdb
