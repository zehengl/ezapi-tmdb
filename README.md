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

A Python wrapper for TMDb API, supporting version [3](https://developers.themoviedb.org/3/getting-started) and [4](https://developers.themoviedb.org/4/getting-started)

## Install

    pip install ezapi-tmdb

## Test

    git clone git@github.com:zehengl/ezapi-tmdb.git
    export api_key="..."
    export username="..."
    export password="..."
    export access_token="..."
    cd ezapi-tmdb
    python setup.py test

Use `$Env:api_key="..."` , `$Env:username="..."`, `$Env:password="..."`, and `$Env:access_token="..."` to set the api key, username, password, and access token environment variables on Windows.

## Usage

1. All endpoints are mapped to functions in a `TMDb` object
2. All query string params are used as keyword arguments

### Version 3 Example

See [documents](https://developers.themoviedb.org/3/getting-started) for detailed API usage.

```python
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
```

### Version 4 Example

```python
from tmdb import TMDb4

# API Read Access Token from the settings page
access_token = "..."

tmdb = TMDb4(access_token)

# create a user access token
request_token = tmdb.create_request_token().get("request_token")
print(f"https://www.themoviedb.org/auth/access?request_token={request_token}")

# click on the link above, sign in, then approve access
resp = tmdb.create_access_token(request_token)

# extract the user access token and account id for v4 api
user_access_token = resp.get("access_token")
account_id = resp.get("account_id")

tmdb.update_access_token(user_access_token)

tmdb.get_list(14105)
tmdb.get_account_favorite_movies(account_id)
```

<hr>

<sup>

## Credits

- [Icon][1] by [Photolio][2]

- Icon from [www.themoviedb.org][3]

</sup>

[1]: https://www.iconfinder.com/icons/4904814/api_app_computer_devolper_interface_programming_icon
[2]: https://www.iconfinder.com/Muhammad_Auns
[3]: https://www.themoviedb.org/about/logos-attribution
