class TMDBException(Exception):
    """Yelp Exception"""
    def __init__(self, *args, **kwargs):
        super(TMDBException, self).__init__(*args, **kwargs)


class InvalidParameter(TMDBException):
    """An invalid parameter occurred"""


class InvalidEndpoint(TMDBException):
    """An invalid endpoint occurred"""
