import re
import os


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

ONE_AUTH_RE = re.compile('^(.+?):(.+)$')

DEFAULT_ONE_AUTH = "~/.one/one_auth"
DEFAULT_ONE_ENDPOINT = "~/.one/one_endpoint"

DEFAULT_CONFIG = os.path.join(CURRENT_DIR, 'config.yml')
DEFAULT_ANSIBLE_VERBOSITY = 2

DEFAULT_REMOTE_DIRECTORY = '/src/'
DEFAULT_RSYNC_EXCLUDE = [
    '.git/',
    '.idea/',
    '.venv/',
    '.tox/',
    'node_modules/',
    '__pycache__/',
]
