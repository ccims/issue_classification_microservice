"""
This type stub file was generated by pyright.
"""

import click
from celery.bin.base import CeleryCommand

"""The ``celery list bindings`` command, used to inspect queue bindings."""
@click.group(name="list")
def list_():
    """Get info from broker.

    Note:

        For RabbitMQ the management plugin is required.
    """
    ...

@list_.command(cls=CeleryCommand)
@click.pass_context
def bindings(ctx):
    """Inspect queue bindings."""
    ...

