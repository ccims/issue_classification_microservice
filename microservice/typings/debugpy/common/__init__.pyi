"""
This type stub file was generated by pyright.
"""

import os
from __future__ import absolute_import, division, print_function, unicode_literals

PROCESS_SPAWN_TIMEOUT = float(os.getenv("DEBUGPY_PROCESS_SPAWN_TIMEOUT", 15))
PROCESS_EXIT_TIMEOUT = float(os.getenv("DEBUGPY_PROCESS_EXIT_TIMEOUT", 5))
