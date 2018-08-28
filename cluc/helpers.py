import click


def note(message):
    if isinstance(message, bytes):
        message = message.decode()
    click.secho(message, fg='green')


def info(message):
    if isinstance(message, bytes):
        message = message.decode()
    click.secho(message, fg='yellow')


def warn(message):
    if isinstance(message, bytes):
        message = message.decode()
    click.secho(message, fg='red')
