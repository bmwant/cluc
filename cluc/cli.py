import os

import click
from click import UsageError, BadParameter

from cluc import cli_options
from cluc.cluster import ClusterManager
from cluc.helpers import info
from cluc.cli_utils import requires_creds
from cluc.utils import rsync_directory
from cluc.tables import Table


@click.group()
@click.version_option()
def cli():
    pass


@cli.command(
    name='sync',
    help='',
)
@click.option(
    '--src',
    help='Directory on local machine which will be synced',
    type=click.Path(),
)
@click.option(
    '--dest',
    required=True,
    help='Location on target machine where to sync source directory',
)
def sync_directory(src, dest):
    if src is None:
        src = os.getcwd()
    rsync_directory(src, '/vagrant/tmp')


@cli.command(
    name='vms',
    help='List all of your created VMs'
)
@requires_creds
def list_vms():
    cinfo = ClusterManager()
    vms = cinfo.list_vms()
    header = ['#ID', 'Name', 'IP', 'State']
    table = Table(header=header, data=vms)
    table.print()


@cli.command(
    name='templates',
    help='List all of your created templates'
)
@requires_creds
def list_templates():
    cmgr = ClusterManager()
    templates = cmgr.list_templates()
    header = ['#ID', 'Name']
    table = Table(header=header, data=templates)
    table.print()


@cli.command(
    name='create',
    help='Create a virtual machine',
)
@requires_creds
def create_vm():
    # from PyInquirer import prompt, Token, style_from_dict
    # from cluc.questions import questions_create
    # answ = prompt(questions_create)
    # print(answ)

    cmgr = ClusterManager()
    template = cmgr.get_template_by_name('misha-immunify360-cpanel-11.66-cloudlinux-7.4')
    res = template.instantiate(name='It is my name')
    print(res)


@cli.command(
    name='info',
    help='Show information about virtual machine',
)
@cli_options.vm_id
@cli_options.vm_name
@requires_creds
def info_vm(vm_id, vm_name):
    pass


@cli.command(
    name='terminate',
    help='Terminate a virtual machine',
)
@cli_options.vm_id
@cli_options.vm_name
@requires_creds
def terminate_vm(vm_id, vm_name):
    if vm_id is not None and vm_name is not None:
        raise UsageError('Provide either VM id or VM name')

    cmgr = ClusterManager()
    if vm_id is not None:
        vm = cmgr.get_vm_by_id(vm_id)
        if vm is None:
            raise BadParameter('No VM with such id %s' % vm_id)

        info('Terminating VM#%s...' % vm_id)
        vm.delete()
        return

    if vm_name is not None:
        vm = cmgr.get_vm_by_name(vm_name)
        if vm is None:
            raise BadParameter('No VM with such name %s' % vm_name)

        info('Terminating VM %s...' % vm_name)
        vm.delete()
        return

    raise UsageError('Provide VM identifier to terminate')


if __name__ == '__main__':
    cli()
