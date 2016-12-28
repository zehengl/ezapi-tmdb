from configparser import ConfigParser
from os import path


config_path = path.abspath(path.dirname(__file__))
config_file = '%s/credentials.conf' % config_path

assert path.isfile(config_file), \
    """
    Please use your credentials for testing
    1. touch tests/credentials.conf
    2. add your credentials in the config file
        [v3]
        api_key = xxxx

        [v4]
        api_key = xxxx
    """

config = ConfigParser()
config.read(config_file)

assert config.get('v3', 'api_key'), 'missing v3 api_key'
assert config.get('v4', 'api_key'), 'missing v4 api_key'

credential_v3 = {
    'api_key': config.get('v3', 'api_key')
}

credential_v4 = {
    'api_key': config.get('v4', 'api_key')
}


def is_error(response):
    """
    Utility function to check if a response is error
    :param response: dict
    :return: boolean
    """
    if type(response) is dict:
        return response.get('status_code') is not None
    elif type(response) is list:
        return response is None
    else:
        return True
