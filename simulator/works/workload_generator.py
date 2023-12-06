import random
import time


class WorkloadGenerator:
    def __init__(self, datacenter, network_bandwidth):
        self.datacenter = datacenter
        self.network_bandwidth = network_bandwidth

    def generate_tasks(self, num_tasks):
        # Generate tasks with random resource requirements and runtimes
        tasks = []
        for i in range(num_tasks):
            cpu_requirement = random.randint(1, 100)
            ram_requirement = random.randint(1, 100)
            disk_requirement = random.randint(1, 100)
            runtime = random.randint(1, 10)
            data_size = random.randint(1, 100000)

            task = Task(
                i,
                cpu_requirement,
                ram_requirement,
                disk_requirement,
                runtime,
                data_size,
            )
            tasks.append(task)

        return tasks

    def submit_tasks(self, tasks):
        for task in tasks:
            available_host = self.datacenter.find_available_host(task)
            if available_host:
                available_host.allocate_task(task)

                # Simulate data transfer to the host
                self.network_bandwidth.transfer_data(task.data_size)

                # Simulate task execution on the host
                time.sleep(task.runtime)

                # Release the task from the host and the network bandwidth
                available_host.release_task(task)

                # Check for any network-related errors during task execution
                if random.random() < self.network_bandwidth.packet_loss_rate:
                    print(
                        "Warning: Task execution may have been affected by network packet loss"
                    )
