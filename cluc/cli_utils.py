import os
from functools import wraps

import click
from PyInquirer import prompt, Token, style_from_dict

from cluc import settings
from cluc.utils import create_dirs
from cluc.questions import questions_credentials, questions_endpoint


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


def note(message):
    click.secho(message, fg='green')


def info(message):
    click.secho(message, fg='yellow')


def warn(message):
    click.secho(message, fg='red')


def init_credentials():
    file_creds = os.path.expanduser(settings.DEFAULT_ONE_AUTH)
    if not os.path.exists(file_creds):
        info('No credentials found! Please provide your account data.')
        credentials = prompt(questions_credentials, style=style)
        create_dirs(file_creds)
        with open(file_creds, 'w') as f:
            creds_line = '{}:{}\n'.format(
                credentials['username'], credentials['password'])
            f.write(creds_line)

    file_endpoint = os.path.expanduser(settings.DEFAULT_ONE_ENDPOINT)
    if not os.path.exists(file_endpoint):
        info('No endpoint specified! Provide XMLRPC URL.')
        endpoint_data = prompt(questions_endpoint, style=style)
        create_dirs(file_endpoint)
        with open(file_endpoint, 'w') as f:
            endpoint_line = '{}\n'.format(endpoint_data['endpoint'])
            f.write(endpoint_line)


def requires_creds(func):
    @wraps(func)
    def inner(*args, **kwargs):
        init_credentials()
        return func(*args, **kwargs)

    return inner
