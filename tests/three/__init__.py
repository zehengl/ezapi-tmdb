import random
import time

import wrapt


@wrapt.decorator
def polite(wrapped, instance, args, kwargs):
    wrapped(*args, **kwargs)
    time.sleep(random.randint(1, 2))
