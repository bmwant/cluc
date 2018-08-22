import click
from click import UsageError, BadParameter

from cluc.cluster import ClusterManager
from cluc.cli_utils import info, requires_creds


@click.group()
@click.version_option()
def cli():
    pass


@cli.command(
    name='list',
    help='List all of your currently running VMs'
)
@requires_creds
def list_vms():
    cinfo = ClusterManager()
    vms = cinfo.list_vms()
    click.echo('\n'.join(vms))


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
