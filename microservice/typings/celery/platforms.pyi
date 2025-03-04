"""
This type stub file was generated by pyright.
"""

import os
import platform as _platform
import signal as _signal
import struct
import sys
from collections import namedtuple
from contextlib import contextmanager
from .local import try_import

"""Platforms.

Utilities dealing with platform specifics: signals, daemonization,
users, groups, and so on.
"""
_setproctitle = try_import('setproctitle')
resource = try_import('resource')
pwd = try_import('pwd')
grp = try_import('grp')
mputil = try_import('multiprocessing.util')
EX_OK = getattr(os, 'EX_OK', 0)
EX_FAILURE = 1
EX_UNAVAILABLE = getattr(os, 'EX_UNAVAILABLE', 69)
EX_USAGE = getattr(os, 'EX_USAGE', 64)
EX_CANTCREAT = getattr(os, 'EX_CANTCREAT', 73)
SYSTEM = _platform.system()
IS_macOS = SYSTEM == 'Darwin'
IS_WINDOWS = SYSTEM == 'Windows'
DAEMON_WORKDIR = '/'
PIDFILE_FLAGS = os.O_CREAT | os.O_EXCL | os.O_WRONLY
PIDFILE_MODE = os.R_OK | os.W_OK << 6 | os.R_OK << 3 | os.R_OK
PIDLOCKED = """ERROR: Pidfile ({0}) already exists.
Seems we're already running? (pid: {1})"""
_range = namedtuple('_range', ('start', 'stop'))
C_FORCE_ROOT = os.environ.get('C_FORCE_ROOT', False)
ROOT_DISALLOWED = """\
Running a worker with superuser privileges when the
worker accepts messages serialized with pickle is a very bad idea!

If you really want to continue then you have to set the C_FORCE_ROOT
environment variable (but please think about this before you do).

User information: uid={uid} euid={euid} gid={gid} egid={egid}
"""
ROOT_DISCOURAGED = """\
You're running the worker with superuser privileges: this is
absolutely not recommended!

Please specify a different user using the --uid option.

User information: uid={uid} euid={euid} gid={gid} egid={egid}
"""
SIGNAMES = sig for sig in dir(_signal) if sig.startswith('SIG') and '_' not in sig
SIGMAP = { getattr(_signal, name): name for name in SIGNAMES }
def isatty(fh):
    """Return true if the process has a controlling terminal."""
    ...

def pyimplementation():
    """Return string identifying the current Python implementation."""
    ...

class LockFailed(Exception):
    """Raised if a PID lock can't be acquired."""
    ...


class Pidfile:
    """Pidfile.

    This is the type returned by :func:`create_pidlock`.

    See Also:
        Best practice is to not use this directly but rather use
        the :func:`create_pidlock` function instead:
        more convenient and also removes stale pidfiles (when
        the process holding the lock is no longer running).
    """
    path = ...
    def __init__(self, path) -> None:
        ...
    
    def acquire(self):
        """Acquire lock."""
        ...
    
    __enter__ = ...
    def is_locked(self):
        """Return true if the pid lock exists."""
        ...
    
    def release(self, *args):
        """Release lock."""
        ...
    
    __exit__ = ...
    def read_pid(self):
        """Read and return the current pid."""
        ...
    
    def remove(self):
        """Remove the lock."""
        ...
    
    def remove_if_stale(self):
        """Remove the lock if the process isn't running.

        I.e. process does not respons to signal.
        """
        ...
    
    def write_pid(self):
        ...
    


PIDFile = Pidfile
def create_pidlock(pidfile):
    """Create and verify pidfile.

    If the pidfile already exists the program exits with an error message,
    however if the process it refers to isn't running anymore, the pidfile
    is deleted and the program continues.

    This function will automatically install an :mod:`atexit` handler
    to release the lock at exit, you can skip this by calling
    :func:`_create_pidlock` instead.

    Returns:
       Pidfile: used to manage the lock.

    Example:
        >>> pidlock = create_pidlock('/var/run/app.pid')
    """
    ...

def fd_by_path(paths):
    """Return a list of file descriptors.

    This method returns list of file descriptors corresponding to
    file paths passed in paths variable.

    Arguments:
        paths: List[str]: List of file paths.

    Returns:
        List[int]: List of file descriptors.

    Example:
        >>> keep = fd_by_path(['/dev/urandom', '/my/precious/'])
    """
    ...

class DaemonContext:
    """Context manager daemonizing the process."""
    _is_open = ...
    def __init__(self, pidfile=..., workdir=..., umask=..., fake=..., after_chdir=..., after_forkers=..., **kwargs) -> None:
        ...
    
    def redirect_to_null(self, fd):
        ...
    
    def open(self):
        ...
    
    __enter__ = ...
    def close(self, *args):
        ...
    
    __exit__ = ...


def detached(logfile=..., pidfile=..., uid=..., gid=..., umask=..., workdir=..., fake=..., **opts):
    """Detach the current process in the background (daemonize).

    Arguments:
        logfile (str): Optional log file.
            The ability to write to this file
            will be verified before the process is detached.
        pidfile (str): Optional pid file.
            The pidfile won't be created,
            as this is the responsibility of the child.  But the process will
            exit if the pid lock exists and the pid written is still running.
        uid (int, str): Optional user id or user name to change
            effective privileges to.
        gid (int, str): Optional group id or group name to change
            effective privileges to.
        umask (str, int): Optional umask that'll be effective in
            the child process.
        workdir (str): Optional new working directory.
        fake (bool): Don't actually detach, intended for debugging purposes.
        **opts (Any): Ignored.

    Example:
        >>> from celery.platforms import detached, create_pidlock
        >>> with detached(
        ...           logfile='/var/log/app.log',
        ...           pidfile='/var/run/app.pid',
        ...           uid='nobody'):
        ... # Now in detached child process with effective user set to nobody,
        ... # and we know that our logfile can be written to, and that
        ... # the pidfile isn't locked.
        ... pidlock = create_pidlock('/var/run/app.pid')
        ...
        ... # Run the program
        ... program.run(logfile='/var/log/app.log')
    """
    ...

def parse_uid(uid):
    """Parse user id.

    Arguments:
        uid (str, int): Actual uid, or the username of a user.
    Returns:
        int: The actual uid.
    """
    ...

def parse_gid(gid):
    """Parse group id.

    Arguments:
        gid (str, int): Actual gid, or the name of a group.
    Returns:
        int: The actual gid of the group.
    """
    ...

def setgroups(groups):
    """Set active groups from a list of group ids."""
    ...

def initgroups(uid, gid):
    """Init process group permissions.

    Compat version of :func:`os.initgroups` that was first
    added to Python 2.7.
    """
    ...

def setgid(gid):
    """Version of :func:`os.setgid` supporting group names."""
    ...

def setuid(uid):
    """Version of :func:`os.setuid` supporting usernames."""
    ...

def maybe_drop_privileges(uid=..., gid=...):
    """Change process privileges to new user/group.

    If UID and GID is specified, the real user/group is changed.

    If only UID is specified, the real user is changed, and the group is
    changed to the users primary group.

    If only GID is specified, only the group is changed.
    """
    ...

class Signals:
    """Convenience interface to :mod:`signals`.

    If the requested signal isn't supported on the current platform,
    the operation will be ignored.

    Example:
        >>> from celery.platforms import signals

        >>> from proj.handlers import my_handler
        >>> signals['INT'] = my_handler

        >>> signals['INT']
        my_handler

        >>> signals.supported('INT')
        True

        >>> signals.signum('INT')
        2

        >>> signals.ignore('USR1')
        >>> signals['USR1'] == signals.ignored
        True

        >>> signals.reset('USR1')
        >>> signals['USR1'] == signals.default
        True

        >>> from proj.handlers import exit_handler, hup_handler
        >>> signals.update(INT=exit_handler,
        ...                TERM=exit_handler,
        ...                HUP=hup_handler)
    """
    ignored = ...
    default = ...
    if hasattr(_signal, 'setitimer'):
        def arm_alarm(self, seconds):
            ...
        
    else:
        ...
    def reset_alarm(self):
        ...
    
    def supported(self, name):
        """Return true value if signal by ``name`` exists on this platform."""
        ...
    
    def signum(self, name):
        """Get signal number by name."""
        ...
    
    def reset(self, *signal_names):
        """Reset signals to the default signal handler.

        Does nothing if the platform has no support for signals,
        or the specified signal in particular.
        """
        ...
    
    def ignore(self, *names):
        """Ignore signal using :const:`SIG_IGN`.

        Does nothing if the platform has no support for signals,
        or the specified signal in particular.
        """
        ...
    
    def __getitem__(self, name):
        ...
    
    def __setitem__(self, name, handler):
        """Install signal handler.

        Does nothing if the current platform has no support for signals,
        or the specified signal in particular.
        """
        ...
    
    def update(self, _d_=..., **sigmap):
        """Set signal handlers from a mapping."""
        ...
    


signals = Signals()
get_signal = signals.signum
install_signal_handler = signals.__setitem__
reset_signal = signals.reset
ignore_signal = signals.ignore
def signal_name(signum):
    """Return name of signal from signal number."""
    ...

def strargv(argv):
    ...

def set_process_title(progname, info=...):
    """Set the :command:`ps` name for the currently running process.

    Only works if :pypi:`setproctitle` is installed.
    """
    ...

if os.environ.get('NOSETPS'):
    def set_mp_process_title(*a, **k):
        """Disabled feature."""
        ...
    
else:
    def set_mp_process_title(progname, info=..., hostname=...):
        """Set the :command:`ps` name from the current process name.

        Only works if :pypi:`setproctitle` is installed.
        """
        ...
    
def get_errno_name(n):
    """Get errno for string (e.g., ``ENOENT``)."""
    ...

@contextmanager
def ignore_errno(*errnos, **kwargs):
    """Context manager to ignore specific POSIX error codes.

    Takes a list of error codes to ignore: this can be either
    the name of the code, or the code integer itself::

        >>> with ignore_errno('ENOENT'):
        ...     with open('foo', 'r') as fh:
        ...         return fh.read()

        >>> with ignore_errno(errno.ENOENT, errno.EPERM):
        ...    pass

    Arguments:
        types (Tuple[Exception]): A tuple of exceptions to ignore
            (when the errno matches).  Defaults to :exc:`Exception`.
    """
    ...

def check_privileges(accept_content):
    ...

if sys.version_info < (2, 7, 7):
    ...
else:
    pack = struct.pack
    unpack = struct.unpack
    unpack_from = struct.unpack_from
