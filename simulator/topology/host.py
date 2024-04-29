"""
This file contains the Host class.
"""


class Host:
    """
    A host in the datacenter.

    Attributes
    ----------
    id : int
        Unique identifier for the host.
    cpu : int
        Number of CPU cores.
    ram : int
        Amount of RAM in GB.
    disk : int
        Amount of disk space in GB.
    power : int
        Power consumption in Watts.

    Methods
    -------
    allocate_task(task)
        Allocate a task to the host.
    release_task(task)
        Release the resources associated with a task.

    Examples
    --------
    >>> host = Host(0, 2, 4, 50, 20)
    >>> print(host)
    Host 0: CPU = 2 IPS, RAM = 4 GB, Disk = 50 GB, Power = 20 W
    >>> host = Host(0, 2, 4, 50, 20, 40.186476, -8.4157114)
    >>> print(host)
    Host 0: CPU = 2 IPS, RAM = 4 GB, Disk = 50 GB, Power = 20 W, Location = (40.186476, -8.4157114)
    """

    def __init__(
        self,
        id: int,
        cpu: int,
        ram: int,
        disk: int,
        power: int,
        latitude: float = 0,
        longitude: float = 0,
        altitude: float = 0,
    ):
        """
        Parameters
        ----------
        id : int
            Unique identifier for the host.
        cpu : int
            Number of CPU cores.
        ram : int
            Amount of RAM in GB.
        disk : int
            Amount of disk space in GB.
        power : int
            Power consumption in Watts.
        latitude : float, optional
            Latitude of the host.
        longitude : float, optional
            Longitude of the host.
        altitude : float, optional
            Altitude of the host.
        """

        self.id = id
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.power = power
        # Optional attributes
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        # Fun fact: The default values of latitude and longitude (0, 0)
        # is usually called the Null Island :)

    def update_location(self, latitude: float, longitude: float, altitude: float = 0):
        """Update the location of the host.

        Parameters
        ----------
        latitude : float
            Latitude of the host.
        longitude : float
            Longitude of the host.
        altitude : float, optional
            Altitude of the host.
        """
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def get_location(self) -> tuple[float, float, float]:
        """Get the location of the host.

        Returns
        -------
        tuple of float
            Tuple containing the latitude, longitude, and altitude of the host.
        """
        return (self.latitude, self.longitude, self.altitude)

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

    def __str__(self):
        output = (
            f"Host {self.id}: CPU = {self.cpu} IPS, RAM = {self.ram} GB, "
            f"Disk = {self.disk} GB, Power = {self.power} W"
        )
        if self.latitude and self.longitude:
            output += (
                f", Location = ({self.latitude}, {self.longitude}, {self.altitude})"
            )

        return output
