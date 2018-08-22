import click
from click import UsageError, BadParameter

from cluc.cluster import ClusterInfo
from cluc.cli_utils import info


@click.group()
@click.version_option()
def cli():
    pass


@cli.command(
    name='list',
    help='List all of your currently running VMs'
)
def list_vms():
    cinfo = ClusterInfo()
    cinfo.list_vms()


@cli.command(
    name='create',
    help='Create a virtual machine',
)
def create_vm():
    pass


@cli.command(
    name='terminate',
    help='Terminate a virtual machine',
)
@click.option(
    '--id',
    'vm_id',
    type=int,
)
@click.option(
    '--name',
    'vm_name',
    type=str,
)
def terminate_vm(vm_id, vm_name):
    if vm_id is not None and vm_name is not None:
        raise UsageError('Provide either VM id or VM name')

    cmgr = ClusterInfo()
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
