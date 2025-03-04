"""
This type stub file was generated by pyright.
"""

from celery.utils.log import get_logger

"""Implementation of the Observer pattern."""
logger = get_logger(__name__)
NONE_ID = _make_id(None)
NO_RECEIVERS = object()
RECEIVER_RETRY_ERROR = """\
Could not process signal receiver %(receiver)s. Retrying %(when)s...\
"""
class Signal:
    """Create new signal.

    Keyword Arguments:
        providing_args (List): A list of the arguments this signal can pass
            along in a :meth:`send` call.
        use_caching (bool): Enable receiver cache.
        name (str): Name of signal, used for debugging purposes.
    """
    receivers = ...
    def __init__(self, providing_args=..., use_caching=..., name=...) -> None:
        ...
    
    def connect(self, *args, **kwargs):
        """Connect receiver to sender for signal.

        Arguments:
            receiver (Callable): A function or an instance method which is to
                receive signals.  Receivers must be hashable objects.

                if weak is :const:`True`, then receiver must be
                weak-referenceable.

                Receivers must be able to accept keyword arguments.

                If receivers have a `dispatch_uid` attribute, the receiver will
                not be added if another receiver already exists with that
                `dispatch_uid`.

            sender (Any): The sender to which the receiver should respond.
                Must either be a Python object, or :const:`None` to
                receive events from any sender.

            weak (bool): Whether to use weak references to the receiver.
                By default, the module will attempt to use weak references to
                the receiver objects.  If this parameter is false, then strong
                references will be used.

            dispatch_uid (Hashable): An identifier used to uniquely identify a
                particular instance of a receiver.  This will usually be a
                string, though it may be anything hashable.

            retry (bool): If the signal receiver raises an exception
                (e.g. ConnectionError), the receiver will be retried until it
                runs successfully. A strong ref to the receiver will be stored
                and the `weak` option will be ignored.
        """
        ...
    
    def disconnect(self, receiver=..., sender=..., weak=..., dispatch_uid=...):
        """Disconnect receiver from sender for signal.

        If weak references are used, disconnect needn't be called.
        The receiver will be removed from dispatch automatically.

        Arguments:
            receiver (Callable): The registered receiver to disconnect.
                May be none if `dispatch_uid` is specified.

            sender (Any): The registered sender to disconnect.

            weak (bool): The weakref state to disconnect.

            dispatch_uid (Hashable): The unique identifier of the receiver
                to disconnect.
        """
        ...
    
    def has_listeners(self, sender=...):
        ...
    
    def send(self, sender, **named):
        """Send signal from sender to all connected receivers.

        If any receiver raises an error, the error propagates back through
        send, terminating the dispatch loop, so it is quite possible to not
        have all receivers called if a raises an error.

        Arguments:
            sender (Any): The sender of the signal.
                Either a specific object or :const:`None`.
            **named (Any): Named arguments which will be passed to receivers.

        Returns:
            List: of tuple pairs: `[(receiver, response), … ]`.
        """
        ...
    
    send_robust = ...
    def __repr__(self):
        """``repr(signal)``."""
        ...
    
    def __str__(self) -> str:
        """``str(signal)``."""
        ...
    


