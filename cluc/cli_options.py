from functools import lru_cache

import click
import yaml

from cluc import settings


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


@lru_cache(maxsize=1)
def read_config():
    with open(settings.DEFAULT_CONFIG) as f:
        return yaml.load(f.read())


def get_oses(answers):
    print(answers)
    config = read_config()
    import pdb; pdb.set_trace()
    print(config)


def get_panels(answers):
    pass


def get_panel_versions(answers):
    pass
