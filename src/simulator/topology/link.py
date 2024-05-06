import random


class Link:
    """
    Represents a network link between two hosts in a datacenter

    Attributes
    ----------
    bandwidth : int
        Represents the maximum data transfer rate in Mbps
    distance : float
        Represents the distance between the two hosts in km
    packet_loss_rate : float, optional
        Represents the probability of packet loss
    is_wired : bool, optional
        Represents whether the link is wired or wireless, by default True.
        This attribute is used to calculate the propagation delay

    Methods
    -------

    """

    def __init__(
        self,
        bandwidth: int,
        distance: float,
        packet_loss_rate: float = 0,
        is_wired: bool = True,
    ):
        self.bandwidth = bandwidth
        self.distance = distance
        self.packet_loss_rate = packet_loss_rate
        self.is_wired = is_wired

    def update_distance(self, distance: float):
        """Update the distance between the two hosts

        Parameters
        ----------
        distance : float
            Distance between the two hosts in km
        """
        self.distance = distance

    def transfer_data(self, data_size):
        # TODO: Implement the transfer_data method

        if data_size > self.bandwidth:
            raise ValueError("Data size exceeds link capacity")

        # https://www.geeksforgeeks.org/delays-in-computer-network/
        transmission_delay = data_size / self.bandwidth

        if self.is_wired:
            propagation_delay = self.distance / 2.1 * 10**5
        else:
            propagation_delay = self.distance / 3 * 10**5

        # Note: in a vacuum the speed is:
        # (in the ait) = 3 * 10**8 m/s
        # (in optical fiber) = 2.1 * 10**8 m/s
        # NOTE: We are using the value as Km/s because the distance is in Km
        # https://www.geeksforgeeks.org/delays-in-computer-network/

        if random.random() < self.packet_loss_rate:
            print("Warning: Data packet lost during transfer")

    def is_available(self, data_size):
        return data_size <= self.bandwidth

    def __str__(self):
        return (
            f"Bandwidth = {self.bandwidth} Mbps, "
            f"Distance = {self.distance} km, "
            f"Packet Loss Rate = {self.packet_loss_rate} %, "
            f"is_wired = {self.is_wired}"
        )
