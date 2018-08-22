from contextlib import suppress

import oca
from oca.pool import WrongIdError, WrongNameError


username = ''
password = ''
endpoint = 'https://'


client = oca.Client('{}:{}'.format(username, password), endpoint)


class ClusterInfo(object):
    def __init__(self):
        self._vm_pool = None
        self._client = oca.Client('{}:{}'.format(username, password), endpoint)

    def get_vm_by_id(self, vm_id):
        with suppress(WrongIdError):
            return self.vm_pool.get_by_id(vm_id)

    def get_vm_by_name(self, vm_name):
        with suppress(WrongNameError):
            return self.vm_pool.get_by_name(vm_name)

    def list_vms(self):
        for vm in self.vm_pool:
            # import pdb; pdb.set_trace()
            ip_list = ', '.join(v.ip for v in vm.template.nics)
            print("{} {} {} (memory: {} MB)".format(vm.name, ip_list, vm.str_state, vm.template.memory))

    @property
    def vm_pool(self):
        if self._vm_pool is None:
            self._vm_pool = oca.VirtualMachinePool(self._client)
        # Update information to retrieve latest data on each call
        self._vm_pool.info()
        return self._vm_pool
