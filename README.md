# ezapi-tmdb

A Python wrapper for TMDb API, supporting version [3](https://developers.themoviedb.org/3/getting-started)

[![Travis](https://img.shields.io/travis/zehengl/ezapi-tmdb.svg)](https://travis-ci.org/zehengl/ezapi-tmdb)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![PyPI - License](https://img.shields.io/pypi/l/ezapi-tmdb.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ezapi-tmdb.svg)
[![PyPI](https://img.shields.io/pypi/v/ezapi-tmdb.svg)](https://pypi.python.org/pypi/ezapi-tmdb)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/zehengl/ezapi-tmdb/0.5.0.svg)

## Install

    pip install ezapi-tmdb

## Test

    git clone git@github.com:zehengl/ezapi-tmdb.git
    export api_key="..."
    export username="..."
    export password="..."
    cd ezapi-tmdb
    python setup.py test

## Usage

1. All endpoints are mapped to funtions in a `TMDb` object
2. All query string params are used keyword arguments

See [documents](https://developers.themoviedb.org/3/getting-started) for detailed API usage.

    from tmdb import TMDb

    api_key = "..."

    tmdb = TMDb(api_key)

    # query string params are used as keyword arguments
    print(tmdb.get_popular_movies(region="US"))
    print(tmdb.get_tvs_on_the_air(page=10))

    # create session_id with username/password login
    username = "..."
    password = "..."
    request_token = tmdb.create_request_token().get("request_token")
    tmdb.create_session_with_login(username, password, request_token)
    session_id = tmdb.create_session(request_token).get("session_id")

    # some endpoints require session_id
    print(tmdb.get_account_details(session_id=session_id))
