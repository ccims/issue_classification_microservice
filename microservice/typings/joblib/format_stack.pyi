"""
This type stub file was generated by pyright.
"""

from sys import version_info
from joblib import _deprecated_format_stack

_deprecated_names = [name for name in dir(_deprecated_format_stack) if not name.startswith("__")]
if version_info[: 2] >= (3, 7):
    def __getattr__(name):
        ...
    
else:
    ...
