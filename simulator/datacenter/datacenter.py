class Datacenter:
    def __init__(self, hosts):
        self.hosts = hosts

    def add_host(self, host):
        self.hosts.append(host)

    def remove_host(self, host):
        self.hosts.remove(host)

    def find_available_host(self, task):
        # Search for a host with enough resources to allocate the task
        for host in self.hosts:
            if host.allocate_task(task):
                return host
        return None

    def release_task(self, host, task):
        host.release_task(task)
