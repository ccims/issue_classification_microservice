"""
This type stub file was generated by pyright.
"""

import os
import re
import sys
import builtins
from collections import namedtuple
from . import local
from celery._state import current_app, current_task
from celery.app import shared_task
from celery.app.base import Celery
from celery.app.task import Task
from celery.app.utils import bugreport
from celery.canvas import chain, chord, chunks, group, maybe_signature, signature, subtask, xmap, xstarmap
from celery.utils import uuid

"""Distributed Task Queue."""
SERIES = 'singularity'
__version__ = '5.0.1'
__author__ = 'Ask Solem'
__contact__ = 'auvipy@gmail.com'
__homepage__ = 'http://celeryproject.org'
__docformat__ = 'restructuredtext'
__keywords__ = 'task job queue distributed messaging actor'
VERSION_BANNER = <Expression>
version_info_t = namedtuple('version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'))
_temp = re.match(r'(\d+)\.(\d+).(\d+)(.+)?', __version__).groups()
VERSION = version_info = version_info_t(int(_temp[0]), int(_temp[1]), int(_temp[2]), _temp[3] or '', '')
if os.environ.get('C_IMPDEBUG'):
    def debug_import(name, locals=..., globals=..., fromlist=..., level=..., real_import=...):
        ...
    
STATICA_HACK = True
if STATICA_HACK:
    ...
def maybe_patch_concurrency(argv=..., short_opts=..., long_opts=..., patches=...):
    """Apply eventlet/gevent monkeypatches.

    With short and long opt alternatives that specify the command line
    option to set the pool, this makes sure that anything that needs
    to be patched is completed as early as possible.
    (e.g., eventlet/gevent monkey patches).
    """
    ...

