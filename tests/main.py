"""
Main file
"""

import time
from simulator.topology import Network


def main():
    topology_dict = {
        "hosts": [
            {
                "id": 0,
                "cpu": 2,
                "ram": 4,
                "disk": 50,
                "power": 20,
                "latitude": 40.22098878904303,
                "longitude": -8.41301886279813,
            },  # CHUC
            {
                "id": 1,
                "cpu": 4,
                "ram": 8,
                "disk": 100,
                "power": 80,
                "latitude": 40.186476,
                "longitude": -8.4157114,  
            },  # DEI
            {
                "id": 2,
                "cpu": 8,
                "ram": 16,
                "disk": 200,
                "power": 200,
                "latitude": 40.20338110718607,
                "longitude": -8.407717459271545,  
            },  # Alma
        ],
        "links": [
            {"host_id1": 0, "host_id2": 1, "bandwidth": 50},
            {"host_id1": 1, "host_id2": 2, "bandwidth": 200},
            {"host_id1": 0, "host_id2": 2, "bandwidth": 50},
        ],
    }

    timeExe = time.time()
    network = Network()
    # network.load_dict(topology_dict)
    network.network_generation_dbscan(200, 8)

    print("Time to execute: ", time.time() - timeExe)

    # network.print_hosts()
    # network.print_links()
    network.plot(plot_labels=True)

    # network.update_host_location(0, 40.20784298173971, -8.42363234639827)  # CHUC -> DQ

    # network.print_hosts()
    # network.print_links()
    # network.plot()


if __name__ == "__main__":
    main()
