class Task:
    """_summary_
    """
    def __init__(self, id, cpu_requirement, ram_requirement, disk_requirement, runtime):
        """_summary_

        :param id: _description_
        :type id: _type_
        :param cpu_requirement: _description_
        :type cpu_requirement: _type_
        :param ram_requirement: _description_
        :type ram_requirement: _type_
        :param disk_requirement: _description_
        :type disk_requirement: _type_
        :param runtime: _description_
        :type runtime: _type_
        """
        self.id = id
        self.cpu_requirement = cpu_requirement
        self.ram_requirement = ram_requirement
        self.disk_requirement = disk_requirement
        self.runtime = runtime
