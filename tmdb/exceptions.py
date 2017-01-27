class TMDbException(Exception):
    """TMdb Exception"""
    def __init__(self, *args, **kwargs):
        super(TMDbException, self).__init__(*args, **kwargs)


class InvalidParameter(TMDbException):
    """An invalid parameter occurred"""


class InvalidEndpoint(TMDbException):
    """An invalid endpoint occurred"""
