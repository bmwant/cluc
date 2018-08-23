import shutil
from collections import namedtuple

import ansible.constants as C
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.utils.display import Display
from ansible.plugins.callback.default import CallbackModule

from cluc import settings


# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
Options = namedtuple('Options', [
    'connection',
    'module_path',
    'forks',
    'become',
    'become_method',
    'become_user',
    'check',
    'diff',
])

options = Options(
    connection='ssh',  # https://docs.ansible.com/ansible/2.6/plugins/connection.html
    module_path=[],
    forks=1,
    become=None,
    become_method=None,
    become_user=None,
    check=False,
    diff=False,
)

# passwords = dict(vault_pass='secret')


def main():
    display = Display(verbosity=settings.DEFAULT_ANSIBLE_VERBOSITY)
    results_callback = CallbackModule()
    results_callback._display = display
    loader = DataLoader()
    loader.set_basedir('/home/user/cl/defence360/dev-utils/rpm-test')

    # create inventory, use path to host config file as source or hosts in a comma separated string
    inventory = InventoryManager(loader=loader, sources='192.168.245.130,')

    # variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.extra_vars = {
        'ssh_user': 'root',
        # 'ansible_ssh_user': 'root',
        # 'ansible_ssh_private_key_file': "/home/user/.ssh/id_rsa",
        'build_system_repo_ids': '',  # check env
        'csf_installed': False,  # check env
        'cwaf_agent_installed': False,  # check env
        'cxs_installed': False,  # check env
        'firewalld_enabled': False,  # check env
        'modsec_vendor_installed': False,  # check env
        'panel_name': 'cpanel',  # check env
        'panel_version': '11.6',  # check env
        'vm_root_passwd': 'plainpassword',  # check env
        'proxy_server': '',  # check env
        'deploy_script_from_git': False,  # check env
    }
    play_source = loader.load_from_file('/home/user/cl/defence360/dev-utils/rpm-test/prepare.yml')[0]
    # play_source['ansible_ssh_user'] = "root"
    # play_source['ansible_ssh_private_key_file'] = "/home/user/.ssh/id_rsa"

    # Create play object, playbook objects use .load instead of init or new methods,
    # this will also automatically create the task objects from the info provided in play_source
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
    tqm = None
    try:
        tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            options=options,
            passwords={},
            stdout_callback=results_callback,
        )
        result = tqm.run(play)
        print(result)
    finally:
        if tqm is not None:
            tqm.cleanup()

        # Remove ansible tmpdir
        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


if __name__ == '__main__':
    main()
