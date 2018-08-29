import os
from functools import wraps

from PyInquirer import prompt, Token, style_from_dict

from cluc import settings
from cluc.utils import create_dirs
from cluc.helpers import info
from cluc.questions import questions_credentials, questions_endpoint


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


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


def get_vm_by_alias(manager, vm_alias):
    try:
        vm_id = int(vm_alias)
        return manager.get_vm_by_id(vm_id)
    except ValueError:
        return manager.get_vm_by_name(vm_alias)


def get_vm_info(vm):
    return {
        'id': vm.id,
        'name': vm.name,
        'uid': vm.uid,
        'uname': vm.uname,
        'gid': vm.gid,
        'gname': vm.gname,
        'state': vm.str_state,
        'lcm_state': vm.str_lcm_state,
    }
