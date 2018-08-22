import os

import attr

from cluc import settings


@attr.s
class Creds(object):
    username = attr.ib()
    password = attr.ib()


def create_dirs(path):
    full_path = os.path.abspath(os.path.expanduser(path))

    if full_path.endswith('/'):  # it's definitely a directory
        dir_path = full_path
    else:
        # path to a file provided, so create a directory container for it
        dir_path = os.path.dirname(full_path)

    os.makedirs(dir_path, exist_ok=True)


def load_credentials():
    file_creds = os.path.expanduser(settings.DEFAULT_ONE_AUTH)
    with open(file_creds) as f:
        data = f.read().strip()

    one_secret = settings.ONE_AUTH_RE.match(data)
    if one_secret:
        username, password = one_secret.groups()
        creds = Creds(username=username, password=password)
        return creds
    else:
        raise ValueError(
            'File %s is corrupted. '
            'Please make sure your credentials are stored in '
            '"username:password" format'
        )


def load_endpoint():
    file_endpoint = os.path.expanduser(settings.DEFAULT_ONE_ENDPOINT)
    with open(file_endpoint) as f:
        data = f.read().strip()

    return data
