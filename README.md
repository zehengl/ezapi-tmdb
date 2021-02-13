<div align="center">
    <img src="https://cdn3.iconfinder.com/data/icons/data-sharing-and-cloud-lineal-style/512/apiprogrammingdevolperinterfaceappcomputer-512.png" alt="logo" height="196">
    <img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_2-d537fb228cf3ded904ef09b136fe3fec72548ebc1fea3fbbd1ad9e36364db38b.svg" alt="yelp" height="96">
</div>

# ezapi-tmdb

![pytest](https://github.com/zehengl/ezapi-tmdb/workflows/pytest/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![PyPI - License](https://img.shields.io/pypi/l/ezapi-tmdb.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ezapi-tmdb.svg)
[![PyPI](https://img.shields.io/pypi/v/ezapi-tmdb.svg)](https://pypi.python.org/pypi/ezapi-tmdb)
[![Downloads](https://pepy.tech/badge/ezapi-tmdb)](https://pepy.tech/project/ezapi-tmdb)

A Python wrapper for TMDb API, supporting version [3](https://developers.themoviedb.org/3/getting-started)

## Install

    pip install ezapi-tmdb

## Test

    git clone git@github.com:zehengl/ezapi-tmdb.git
    export api_key="..."
    export username="..."
    export password="..."
    cd ezapi-tmdb
    python setup.py test

Use `$Env:api_key="..."` , `$Env:username="..."`, and `$Env:password="..."` to set the api key, username, and password environment variables on Windows.

## Usage

1. All endpoints are mapped to functions in a `TMDb` object
2. All query string params are used as keyword arguments

See [documents](https://developers.themoviedb.org/3/getting-started) for detailed API usage.

    from tmdb import TMDb3

    api_key = "..."

    tmdb = TMDb3(api_key)

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

    # store global options, language / region for example
    tmdb.set_options(language="de", region="de")
    tmdb.get_trending("all", "week")

    # reset global options
    tmdb.reset_options()

    # configure image languages globally
    tmdb.set_options(include_image_language=["en", "null"])
    tmdb.get_movie_images(597)

    # url param per request would overwrite global options
    tmdb.get_movie_images(597, include_image_language=["de", "fr"])

<hr>

<sup>

## Credits

- [Icon][1] by [Photolio][2]

- Icon from [www.themoviedb.org][3]

</sup>

[1]: https://www.iconfinder.com/icons/4904814/api_app_computer_devolper_interface_programming_icon
[2]: https://www.iconfinder.com/Muhammad_Auns
[3]: https://www.themoviedb.org/about/logos-attribution
