import os

import click
from PyInquirer import prompt

from cluc import settings
from cluc.utils import create_dirs
from cluc.questions import questions_credentials


def note(message):
    click.secho(message, fg='green')


def info(message):
    click.secho(message, fg='yellow')


def warn(message):
    click.secho(message, fg='red')


def init_credentials():
    if not os.path.exists(settings.DEFAULT_ONE_AUTH):
        info('No credentials found! Please provide your account data.')
        credentials = prompt(questions_credentials)
        create_dirs(settings.DEFAULT_ONE_AUTH)
        with open(settings.DEFAULT_ONE_AUTH, 'w') as f:
            creds_line = '{}:{}'.format(
                credentials['username'], credentials['password'])
            f.write(creds_line)
