from __future__ import print_function
import json


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def json_to_python(data):
    try:
        from types import SimpleNamespace as Namespace
    except ImportError:
        # Python 2.x fallback
        from argparse import Namespace

    python_obj = json.loads(data, object_hook=lambda d: Namespace(**d))

    return python_obj
