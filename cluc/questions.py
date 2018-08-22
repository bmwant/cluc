from PyInquirer import Separator


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
        'choices': [
            'Ubuntu',
            Separator(),
            'CentOS 6',
            'CentOS 7',
            'CloudLinux',
        ]
    },
    {
        'type': 'list',
        'name': 'panel_name',
        'message': 'Choose panel:',
        'choices': [
            'CPanel',
            'Plesk',
        ]
    },
    {
        'type': 'list',
        'name': 'panel_version',
        'message': 'Choose panel version:',
        'choices': [
            '17',
            '15',
            '13',
            '11',
        ]
    },

]
