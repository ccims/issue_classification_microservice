"""
This type stub file was generated by pyright.
"""

import contextlib

@contextlib.contextmanager
def cwd(dirname):
    """A context manager for operating in a different directory."""
    ...

def iter_all_files(root, prune_dir=..., exclude_file=...):
    """Yield (dirname, basename, filename) for each file in the tree.

    This is an alternative to os.walk() that flattens out the tree and
    with filtering.
    """
    ...

def iter_tree(root, prune_dir=..., exclude_file=...):
    """Yield (dirname, files) for each directory in the tree.

    The list of files is actually a list of (basename, filename).

    This is an alternative to os.walk() with filtering."""
    ...

