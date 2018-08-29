from contextlib import suppress

import oca
from oca.pool import WrongIdError, WrongNameError

from cluc.utils import load_credentials, load_endpoint


__all__ = ('ClusterManager',)


class ClusterBase(object):
    _client = None  # Reuse client within a process

    def __init__(self, *, username=None, password=None, endpoint=None):
        self._vm_pool = None
        self._templates_pool = None
        self._filter = -3
        self.username = username
        self.password = password
        self.endpoint = endpoint
        self._ensure_account_data()

    def _ensure_account_data(self):
        if not self.username or not self.password:
            creds = load_credentials()
            self.username = creds.username
            self.password = creds.password
        if not self.endpoint:
            self.endpoint = load_endpoint()

    @property
    def vm_pool(self):
        if self._vm_pool is None:
            self._vm_pool = oca.VirtualMachinePool(self.client)
        # Update information to retrieve latest data on each call
        self._vm_pool.info(filter=self._filter)
        return self._vm_pool

    @property
    def templates_pool(self):
        if self._templates_pool is None:
            self._templates_pool = oca.VmTemplatePool(self.client)
        self._templates_pool.info()
        return self._templates_pool

    @property
    def client(self):
        if self._client is None:
            self._client = oca.Client(
                '{}:{}'.format(self.username, self.password),
                self.endpoint
            )

        return self._client


class ClusterManager(ClusterBase):

    SHOW_ALL_FLAG = -2

    def get_vm_by_id(self, vm_id):
        with suppress(WrongIdError):
            return self.vm_pool.get_by_id(vm_id)

    def get_vm_by_name(self, vm_name):
        with suppress(WrongNameError):
            return self.vm_pool.get_by_name(vm_name)

    def get_template_by_name(self, template_name):
        with suppress(WrongNameError):
            return self.templates_pool.get_by_name(template_name)

    @staticmethod
    def get_vm_ips(vm) -> list:
        ips = []
        for n in vm.template.nics:
            if hasattr(n, 'ip'):
                ips.append(n.ip)
            elif hasattr(n, 'ip6'):
                ips.append(n.ip6)
            else:
                # logger error
                print('Bad NIC %s' % n)
        return ips

    def list_vms(self, show_all=False) -> list:
        vms_desc = []
        pool = self.vm_pool
        if show_all:
            pool.info(filter=self.SHOW_ALL_FLAG)
        for vm in pool:
            ip_list = '\n'.join(self.get_vm_ips(vm))
            # vm.name, ip_list, vm.str_state, vm.template.memory))
            vms_desc.append([vm.id, vm.name, ip_list, vm.str_state])
        return vms_desc

    def list_templates(self, show_all=False) -> list:
        templates_desc = []
        pool = self.templates_pool
        if show_all:
            pool.info(filter=self.SHOW_ALL_FLAG)
        for template in pool:
            templates_desc.append([template.id, template.name])
        return templates_desc

    def get_template_id_by_name(self, template_name):
        templates_pool = oca.VmTemplatePool(self.client)
        templates_pool.info()
        for template in templates_pool:
            import pdb; pdb.set_trace()
            print(template)


