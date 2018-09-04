from PyInquirer import Separator

from cluc.cli_options import get_oses, get_panels, get_panel_versions


questions_credentials = [
    {
        'type': 'input',
        'name': 'username',
        'message': 'Enter your username',
    },
    {
        'type': 'password',
        'name': 'password',
        'message': 'Enter your password',
    },
]

questions_endpoint = [
    {
        'type': 'input',
        'name': 'endpoint',
        'message': 'Enter RPC endpoint',
    },
]


questions_create = [
    {
        'type': 'list',
        'name': 'os',
        'message': 'Select operating system to use:',
        'choices': [get_oses],
    },
    {
        'type': 'list',
        'name': 'panel_name',
        'message': 'Choose panel:',
        'choices': get_panels,
    },
    {
        'type': 'list',
        'name': 'panel_version',
        'message': 'Choose panel version:',
        'choices': get_panel_versions,
    },
    {
        'type': 'confirm',
        'name': 'csf_installed',
        'message': 'Install ConfigServer Firewall?',
        'default': False,
    },
    {
        'type': 'confirm',
        'name': 'cwaf_agent_installed',
        'message': 'Install Comodo Wep Application Firewall?',
        'default': False,
    },
    {
        'type': 'confirm',
        'name': 'cxs_installed',
        'message': 'Install ConfigServer eXploit Scanner?',
        'default': False,
    },
]
