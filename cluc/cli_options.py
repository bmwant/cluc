import click


vm_id = click.option(
    '--id',
    'vm_id',
    type=int,
)

vm_name = click.option(
    '--name',
    'vm_name',
    type=str,
)

show_all = click.option(
    '--all',
    'show_all',
    is_flag=True,
    default=False,
)
