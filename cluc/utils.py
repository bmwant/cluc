import os
import subprocess

import attr

from cluc import settings
from cluc.helpers import info, warn


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


def get_excludes(excludes: list) -> list:
    return ['--exclude=%s' % ex for ex in excludes]


def rsync_directory(src, dst, *, verbose=True):
    destination = 'root@192.168.245.9:/vagrant/tmp'
    cmd = [
        'rsync', '-avrz', '--cvs-exclude',
        *get_excludes(settings.DEFAULT_RSYNC_EXCLUDE),
        src, destination
    ]
    res = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if res.returncode:
        warn(res.stderr)
        raise RuntimeError('Failed to sync directory')

    if verbose:
        info(res.stdout)
