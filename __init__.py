import logging

def logs(cls):
    cls._log = logging.getLogger(f"{cls.__module__}.{cls.__name__}")
    return cls
