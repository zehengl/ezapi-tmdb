import requests
import wrapt

ENDPOINT = "https://api.themoviedb.org"


def any_required_kwargs(*required_kwargs_list):
    """
    Decorator to check if criteria of required kwargs are met

    Raises:
        RuntimeError: a bad client request

    Returns:
        func: decorated function
    """

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        compliances = [
            all([kwarg in kwargs for kwarg in required_kwargs])
            for required_kwargs in required_kwargs_list
        ]

        if any(compliances):
            return wrapped(*args, **kwargs)

        compliant_sets = [
            f'({" and ".join(required_kwargs)})'
            for required_kwargs in required_kwargs_list
        ]
        msg = f"required kwargs: {' or '.join(compliant_sets)}"

        raise RuntimeError(f"{msg}")

    return wrapper


@wrapt.decorator
def process_response(wrapped, instance, args, kwargs):
    """
    Decorator to process requests.Response

    Raises:
        Exception: Service Unavailable

    Returns:
        dict: json data
    """

    try:
        resp = wrapped(*args, **kwargs)

    except (requests.ConnectionError, requests.Timeout) as e:
        raise Exception("Service Unavailable") from e

    else:
        resp.raise_for_status()
        return resp.json()
