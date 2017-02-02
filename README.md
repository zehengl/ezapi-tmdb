ezapi-tmdb
==========

A Python wrapper for TMDb API, supporting version [3](https://developers.themoviedb.org/3/getting-started)

[![Travis](https://img.shields.io/travis/zehengl/ezapi-tmdb.svg)](https://travis-ci.org/zehengl/ezapi-tmdb)[![PyPI](https://img.shields.io/pypi/v/ezapi-tmdb.svg)](https://pypi.python.org/pypi/ezapi-tmdb)[![Coveralls](https://img.shields.io/coveralls/zehengl/ezapi-tmdb.svg)](https://coveralls.io/github/zehengl/ezapi-tmdb)[![Code Climate](https://img.shields.io/codeclimate/github/zehengl/ezapi-tmdb.svg)](https://codeclimate.com/github/zehengl/ezapi-tmdb)

* Implement all endpoints
* Provide CLI
* Include unit tests

# Install
```bash
pip install ezapi_tmdb
```

# Test
1. Clone down the repo
    ```bash
    git clone git@github.com:zehengl/ezapi-tmdb.git
    cd ezapi-tmdb
    ```
    
2. Create a config file to store your api key for testing
    ```bash
    touch tests/credentials.conf
    ```
    
3. Put donw your api key as follows
    ```
    [v3]
    api_key = xxxx

    [v4]
    api_key = xxxx
    ```
    
4. Run the tests
    ```bash
    python setup.py test
    ```

# Contact

Zeheng Li

imzehengl@gmail.com