class Host:
    """
    A host in the datacenter.
    """

    def __init__(self, id, cpu, ram, disk, power):
        self.id = id
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.power = power

    def allocate_task(self, task):
        # Check if the host has enough resources to allocate the task
        if (
            self.cpu >= task.cpu_requirement
            and self.ram >= task.ram_requirement
            and self.disk >= task.disk_requirement
        ):
            # Allocate the task to the host
            self.cpu -= task.cpu_requirement
            self.ram -= task.ram_requirement
            self.disk -= task.disk_requirement
            return True
        else:
            # Return False if the host does not have enough resources
            return False

    def release_task(self, task):
        # Release the resources associated with the task
        self.cpu += task.cpu_requirement
        self.ram += task.ram_requirement
        self.disk += task.disk_requirement