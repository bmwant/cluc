from contextlib import suppress

import oca
from oca.pool import WrongIdError, WrongNameError


class ClusterManager(object):

    _client = None  # Reuse client within a process

    def __init__(self):
        self._vm_pool = None
        self.username = ''
        self.password = ''
        self.endpoint = ''

    def get_vm_by_id(self, vm_id):
        with suppress(WrongIdError):
            return self.vm_pool.get_by_id(vm_id)

    def get_vm_by_name(self, vm_name):
        with suppress(WrongNameError):
            return self.vm_pool.get_by_name(vm_name)

    def list_vms(self) -> list:
        vms_desc = []
        for vm in self.vm_pool:
            ip_list = ', '.join(v.ip for v in vm.template.nics)
            desc = '{} {} {}'.format(vm.name, ip_list, vm.str_state)
            # print("{} {} {} (memory: {} MB)".format(vm.name, ip_list, vm.str_state, vm.template.memory))\
            vms_desc.append(desc)
        return vms_desc

    @property
    def vm_pool(self):
        if self._vm_pool is None:
            self._vm_pool = oca.VirtualMachinePool(self.client)
        # Update information to retrieve latest data on each call
        self._vm_pool.info()
        return self._vm_pool

    @property
    def client(self):
        if self._client is None:
            self._client = oca.Client(
                '{}:{}'.format(self.username, self.password),
                self.endpoint
            )
            
        return self._client
