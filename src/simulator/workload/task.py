class Task:
    """_summary_"""

    def __init__(
        self,
        id: int,
        cpu_requirement: int,
        ram_requirement: int,
        disk_requirement: int,
        runtime: int,
    ):
        """Constructor Method

        Parameters
        ----------
        id : int
            _description_
        cpu_requirement : int
            _description_
        ram_requirement : int
            _description_
        disk_requirement : int
            _description_
        runtime : int
            _description_
        """
        self.id = id
        self.cpu_requirement = cpu_requirement
        self.ram_requirement = ram_requirement
        self.disk_requirement = disk_requirement
        self.runtime = runtime
