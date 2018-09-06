import os

import click
from click import BadParameter

from cluc import cli_options
from cluc import settings
from cluc.cluster import ClusterManager
from cluc.helpers import info
from cluc.cli_utils import requires_creds, get_vm_by_alias, get_vm_info
from cluc.utils import rsync_directory
from cluc.tables import Table


@click.group()
@click.version_option()
def cli():
    pass


@cli.command(
    name='sync',
    help='Copy local directory to the remote with a help of rsync',
)
@click.option(
    '--src',
    help='Directory on local machine which will be synced',
    type=click.Path(),
)
@click.option(
    '--dest',
    default=settings.DEFAULT_REMOTE_DIRECTORY,
    help='Location on target machine where to sync source directory',
)
def sync_directory(src, dest):
    if src is None:
        src = os.getcwd()
    remote = 'root@192.168.245.9'
    remote = 'root@192.168.245.45'
    rsync_directory(src, remote, dest)


@cli.command(
    name='provision',
    help='',
)
def provision_vm():
    from cluc.ansible_wrapper import main
    main()


@cli.command(
    name='vms',
    help='List of your (all) created VMs'
)
@cli_options.show_all
@requires_creds
def list_vms(show_all):
    cinfo = ClusterManager()
    vms = cinfo.list_vms(show_all=show_all)
    header = ['#ID', 'Name', 'IP', 'State']
    table = Table(header=header, data=vms)
    table.print()


@cli.command(
    name='templates',
    help='List of your (all) created templates'
)
@cli_options.show_all
@requires_creds
def list_templates(show_all):
    cmgr = ClusterManager()
    templates = cmgr.list_templates(show_all=show_all)
    header = ['#ID', 'Name']
    table = Table(header=header, data=templates)
    table.print()


@cli.command(
    name='create',
    help='Create a virtual machine',
)
@requires_creds
def create_vm():
    from PyInquirer import prompt, Token, style_from_dict
    from cluc.questions import questions_create
    answ = prompt(questions_create)
    print(answ)

    # cmgr = ClusterManager()
    # template = cmgr.get_template_by_name('misha-immunify360-cpanel-11.66-cloudlinux-7.4')
    # res = template.instantiate(name='It is my name')
    # print(res)


@cli.command(
    name='info',
    help='Show information about virtual machine',
)
@click.argument('vm_alias')
@requires_creds
def info_vm(vm_alias):
    cmgr = ClusterManager()
    vm = get_vm_by_alias(cmgr, vm_alias)
    vm_info = get_vm_info(vm)
    header = ['PROPERTY', 'VALUE']
    table = Table(header=header, data=vm_info.items(), porcelain=True)
    table.print()


@cli.command(
    name='terminate',
    help='Terminate a virtual machine',
)
@click.argument('vm_alias')
@requires_creds
def terminate_vm(vm_alias):
    cmgr = ClusterManager()
    vm = get_vm_by_alias(cmgr, vm_alias)
    if vm is not None:
        raise BadParameter('No VM with such id or name %s' % vm_alias)

    info('Terminating VM %s...' % vm.name)
    vm.delete()


if __name__ == '__main__':
    cli()
