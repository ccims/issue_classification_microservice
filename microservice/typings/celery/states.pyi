"""
This type stub file was generated by pyright.
"""

"""Built-in task states.

.. _states:

States
------

See :ref:`task-states`.

.. _statesets:

Sets
----

.. state:: READY_STATES

READY_STATES
~~~~~~~~~~~~

Set of states meaning the task result is ready (has been executed).

.. state:: UNREADY_STATES

UNREADY_STATES
~~~~~~~~~~~~~~

Set of states meaning the task result is not ready (hasn't been executed).

.. state:: EXCEPTION_STATES

EXCEPTION_STATES
~~~~~~~~~~~~~~~~

Set of states meaning the task returned an exception.

.. state:: PROPAGATE_STATES

PROPAGATE_STATES
~~~~~~~~~~~~~~~~

Set of exception states that should propagate exceptions to the user.

.. state:: ALL_STATES

ALL_STATES
~~~~~~~~~~

Set of all possible states.

Misc
----

"""
PRECEDENCE = ['SUCCESS', 'FAILURE', None, 'REVOKED', 'STARTED', 'RECEIVED', 'REJECTED', 'RETRY', 'PENDING']
PRECEDENCE_LOOKUP = dict(zip(PRECEDENCE, range(0, len(PRECEDENCE))))
NONE_PRECEDENCE = PRECEDENCE_LOOKUP[None]
def precedence(state):
    """Get the precedence index for state.

    Lower index means higher precedence.
    """
    ...

class state(str):
    """Task state.

    State is a subclass of :class:`str`, implementing comparison
    methods adhering to state precedence rules::

        >>> from celery.states import state, PENDING, SUCCESS

        >>> state(PENDING) < state(SUCCESS)
        True

    Any custom state is considered to be lower than :state:`FAILURE` and
    :state:`SUCCESS`, but higher than any of the other built-in states::

        >>> state('PROGRESS') > state(STARTED)
        True

        >>> state('PROGRESS') > state('SUCCESS')
        False
    """
    def __gt__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    


PENDING = 'PENDING'
RECEIVED = 'RECEIVED'
STARTED = 'STARTED'
SUCCESS = 'SUCCESS'
FAILURE = 'FAILURE'
REVOKED = 'REVOKED'
REJECTED = 'REJECTED'
RETRY = 'RETRY'
IGNORED = 'IGNORED'
READY_STATES = frozenset(SUCCESS, FAILURE, REVOKED)
UNREADY_STATES = frozenset(PENDING, RECEIVED, STARTED, REJECTED, RETRY)
EXCEPTION_STATES = frozenset(RETRY, FAILURE, REVOKED)
PROPAGATE_STATES = frozenset(FAILURE, REVOKED)
ALL_STATES = frozenset(PENDING, RECEIVED, STARTED, SUCCESS, FAILURE, RETRY, REVOKED)
