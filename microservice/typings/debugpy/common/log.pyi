"""
This type stub file was generated by pyright.
"""

import contextlib
import functools
import os
import sys
import threading

LEVELS = ("debug", "info", "warning", "error")
log_dir = os.getenv("DEBUGPY_LOG_DIR")
timestamp_format = "09.3f"
_lock = threading.RLock()
_tls = threading.local()
_files = {  }
_levels = set()
class LogFile(object):
    def __init__(self, filename, file, levels=..., close_file=...) -> None:
        ...
    
    @property
    def levels(self):
        ...
    
    @levels.setter
    def levels(self, value):
        ...
    
    def write(self, level, output):
        ...
    
    def close(self):
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
    


class NoLog(object):
    file = ...
    __bool__ = ...
    def close(self):
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
    


def newline(level=...):
    ...

def write(level, text, _to_files=...):
    ...

def write_format(level, format_string, *args, **kwargs):
    ...

debug = functools.partial(write_format, "debug")
info = functools.partial(write_format, "info")
warning = functools.partial(write_format, "warning")
def error(*args, **kwargs):
    """Logs an error.

    Returns the output wrapped in AssertionError. Thus, the following::

        raise log.error(...)

    has the same effect as::

        log.error(...)
        assert False, fmt(...)
    """
    ...

def swallow_exception(format_string=..., *args, **kwargs):
    """Logs an exception with full traceback.

    If format_string is specified, it is formatted with fmt(*args, **kwargs), and
    prepended to the exception traceback on a separate line.

    If exc_info is specified, the exception it describes will be logged. Otherwise,
    sys.exc_info() - i.e. the exception being handled currently - will be logged.

    If level is specified, the exception will be logged as a message of that level.
    The default is "error".
    """
    ...

def reraise_exception(format_string=..., *args, **kwargs):
    """Like swallow_exception(), but re-raises the current exception after logging it.
    """
    ...

def to_file(filename=..., prefix=..., levels=...):
    """Starts logging all messages at the specified levels to the designated file.

    Either filename or prefix must be specified, but not both.

    If filename is specified, it designates the log file directly.

    If prefix is specified, the log file is automatically created in options.log_dir,
    with filename computed as prefix + os.getpid(). If log_dir is None, no log file
    is created, and the function returns immediately.

    If the file with the specified or computed name is already being used as a log
    file, it is not overwritten, but its levels are updated as specified.

    The function returns an object with a close() method. When the object is closed,
    logs are not written into that file anymore. Alternatively, the returned object
    can be used in a with-statement:

        with log.to_file("some.log"):
            # now also logging to some.log
        # not logging to some.log anymore
    """
    ...

@contextlib.contextmanager
def prefixed(format_string, *args, **kwargs):
    """Adds a prefix to all messages logged from the current thread for the duration
    of the context manager.
    """
    ...

def describe_environment(header):
    ...

stderr = LogFile("<stderr>", sys.stderr, levels=os.getenv("DEBUGPY_LOG_STDERR", "warning error").split(), close_file=False)
