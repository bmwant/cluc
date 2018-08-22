import re


ONE_AUTH_RE = re.compile('^(.+?):(.+)$')

DEFAULT_ONE_AUTH = "~/.one/one_auth"
DEFAULT_ONE_ENDPOINT = "~/.one/one_endpoint"
