import re


ONE_AUTH_RE = re.compile('^(.+?):(.+)$')

DEFAULT_ONE_AUTH = "~/.one/one_auth"
DEFAULT_ONE_ENDPOINT = "~/.one/one_endpoint"


DEFAULT_ANSIBLE_VERBOSITY = 2

DEFAULT_RSYNC_EXCLUDE = [
    '.git/',
    '.idea/',
    '.venv/',
    '.tox/',
    'node_modules/',
    '__pycache__/',
]
