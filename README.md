<div align="center">
    <img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_2-d537fb228cf3ded904ef09b136fe3fec72548ebc1fea3fbbd1ad9e36364db38b.svg" alt="yelp" height="96">
</div>

# ezapi-tmdb

[![pytest](https://github.com/zehengl/ezapi-tmdb/actions/workflows/pytest.yml/badge.svg)](https://github.com/zehengl/ezapi-tmdb/actions/workflows/pytest.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![all-contributors](https://img.shields.io/github/all-contributors/zehengl/ezapi-tmdb)
![PyPI - License](https://img.shields.io/pypi/l/ezapi-tmdb.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ezapi-tmdb.svg)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ezapi-tmdb)
[![Downloads](https://static.pepy.tech/badge/ezapi-tmdb)](https://pepy.tech/project/ezapi-tmdb)
[![GitHub Pages](https://github.com/zehengl/ezapi-tmdb/actions/workflows/gh-deploy.yml/badge.svg)](https://github.com/zehengl/ezapi-tmdb/actions/workflows/gh-deploy.yml)

A Python wrapper for TMDb API, supporting version [3](https://developers.themoviedb.org/3/getting-started) and [4](https://developers.themoviedb.org/4/getting-started)

## Install

From [PyPi](https://pypi.org/project/ezapi-tmdb/)

    pip install ezapi-tmdb

From [GitHub](https://github.com/zehengl/ezapi-tmdb)

    pip install git+https://github.com/zehengl/ezapi-tmdb.git

## Usage

1. All endpoints are mapped to functions in a `TMDb` object
2. All query string params are used as keyword arguments

### Version 3 Example

See [Version 3 documents](https://developers.themoviedb.org/3/getting-started) for detailed API usage.

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

See [Version 4 documents](https://developers.themoviedb.org/4/getting-started) for detailed API usage.

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

## Test

```bash
git clone git@github.com:zehengl/ezapi-tmdb.git
cd ezapi-tmdb
export tmdb_api_key="..."
export tmdb_username="..."
export tmdb_password="..."
export tmdb_access_token="..."
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements-test.txt
pytest
```

Use `$Env:tmdb_api_key="..."` , `$Env:tmdb_username="..."`, `$Env:tmdb_password="..."`, and `$Env:tmdb_access_token="..."` to set the api key, username, password, and access token environment variables on Windows.

## Credits

- Icon from [www.themoviedb.org][1]

[1]: https://www.themoviedb.org/about/logos-attribution

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Cologler"><img src="https://avatars.githubusercontent.com/u/10906962?v=4?s=100" width="100px;" alt="Cologler"/><br /><sub><b>Cologler</b></sub></a><br /><a href="https://github.com/zehengl/ezapi-tmdb/commits?author=Cologler" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rafaelpierre"><img src="https://avatars.githubusercontent.com/u/13171938?v=4?s=100" width="100px;" alt="Rafael Pierre"/><br /><sub><b>Rafael Pierre</b></sub></a><br /><a href="https://github.com/zehengl/ezapi-tmdb/commits?author=rafaelpierre" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/joselimajr"><img src="https://avatars.githubusercontent.com/u/3194122?v=4?s=100" width="100px;" alt="joselimajr"/><br /><sub><b>joselimajr</b></sub></a><br /><a href="#ideas-joselimajr" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
