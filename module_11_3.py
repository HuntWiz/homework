import inspect
from urllib import request
import sys


def introspection_info(obj):
    info = {}
    info.update({'type': type(obj)})
    info.update({'attribute': list(attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__"))})
    info.update({'methods': list(attr for attr in dir(obj) if callable(getattr(obj, attr)) and attr.startswith("__") )})
    info.update({'module': sys.modules[__name__]})
    return info


print(introspection_info(287))