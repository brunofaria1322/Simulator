import random
import time



class Link:
    """
    Represents a network link between two hosts in a datacenter
    """

    def __init__(self, capacity, latency, packet_loss_rate):
        self.capacity = (
            capacity  # Represents the maximum data transfer rate in bytes per second
        )
        self.latency = (
            latency  # Represents the time delay for data transmission in seconds
        )
        self.packet_loss_rate = (
            packet_loss_rate  # Represents the probability of data packets being lost
        )

    def transfer_data(self, data_size):
        if data_size > self.capacity:
            raise ValueError("Data size exceeds link capacity")

        # Simulate data transfer by applying latency and packet loss
        time_taken = self.latency + data_size / self.capacity
        if random.random() < self.packet_loss_rate:
            print("Warning: Data packet lost during transfer")
        else:
            time.sleep(time_taken)

    def is_available(self, data_size):
        return data_size <= self.capacity
