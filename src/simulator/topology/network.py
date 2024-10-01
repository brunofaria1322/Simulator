"""
Topology class file
"""

import math
import os
import json
import requests
from geopy.distance import distance

from .link import Link
from .host import Host
import networkx as nx
import matplotlib.pyplot as plt

from contextily import add_basemap
import geopandas


"""
TODO: ADD MOBILITY MODELS FROM SUMO

in sumo:
important: --fcd-output.geo to give latitude and longitude
sumo -c config.sumocfg --fcd-output.geo 1 --fcd-output fcd-output-file.xml

This will probably be added to the envirnoment updating ts to ts
1. Read the xml
2. add a create/delete or update location of each car
"""


class Network:
    """This class represents the network

    Attributes
    ----------
    G : nx.Graph
        NetworkX Graph representing the network
    id : int
        Internal ID counter

    Methods
    -------
    """

    def __init__(self):
        """Constructor Method"""
        self.G = nx.Graph()
        self.id = 0

        # SUMO
        self.sumo_data = {}
        # for plotting
        self.minlat = 90
        self.maxlat = -90
        self.minlon = 180
        self.maxlon = -180

    def load_sumo_data(self, file_path: str = "", force_read_xml: bool = False):
        """Initialise network from SUMO output file

        If the sumo_data.json file exists, it will load the data from it instead of the XML file, for faster access.

        Parameters
        ----------
        file_path : str, optional
            File path to SUMO output file. Must be XML!
        force_read_xml : bool, optional
            Force reading the XML file, by default False

        Raises
        ------
        FileNotFoundError
            If file does not exist
        TypeError
            If file is not XML
        """

        # Check if sumo_data.json exists
        if not force_read_xml and os.path.isfile("sumo_data.json"):
            print(
                "Found a sumo_data.json file. Loading data from it instead. If you want to reload the sumo data, delete sumo_data.json file."
            )
            with open("sumo_data.json", "r") as file:
                self.sumo_data = {
                    float(ts): value for (ts, value) in json.load(file).items()
                }

            # update min and max lat and lon
            for ts in self.sumo_data:
                for vehicle in self.sumo_data[ts]:
                    vehicle_x = self.sumo_data[ts][vehicle]["x"]
                    vehicle_y = self.sumo_data[ts][vehicle]["y"]
                    # update min and max lat and lon
                    if vehicle_x < self.minlon:
                        self.minlon = vehicle_x
                    if vehicle_x > self.maxlon:
                        self.maxlon = vehicle_x
                    if vehicle_y < self.minlat:
                        self.minlat = vehicle_y
                    if vehicle_y > self.maxlat:
                        self.maxlat = vehicle_y
            return

        if file_path == "":
            raise FileNotFoundError("No JSON file found and no XML file provided")

        # Verify if file is XML
        if not file_path.endswith(".xml"):
            raise TypeError("File must be XML")

        # Verify if file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError("File not found")

        # Read the xml file
        from xml.etree import ElementTree

        tree = ElementTree.parse(file_path)
        root = tree.getroot()

        for timestep in root.findall("timestep"):
            time = float(timestep.get("time") or 0.0)
            self.sumo_data[time] = {}
            for vehicle in timestep.findall("vehicle"):
                vehicle_id = vehicle.get("id")
                self.sumo_data[time][vehicle_id] = {}
                vehicle_x = float(vehicle.get("x") or 0.0)  # longitude
                vehicle_y = float(vehicle.get("y") or 0.0)  # latitude
                # update min and max lat and lon
                if vehicle_x < self.minlon:
                    self.minlon = vehicle_x
                if vehicle_x > self.maxlon:
                    self.maxlon = vehicle_x
                if vehicle_y < self.minlat:
                    self.minlat = vehicle_y
                if vehicle_y > self.maxlat:
                    self.maxlat = vehicle_y

                vehicle_angle = float(vehicle.get("angle") or 0.0)
                vehicle_speed = float(vehicle.get("speed") or 0.0)

                self.sumo_data[time][vehicle_id]["x"] = vehicle_x
                self.sumo_data[time][vehicle_id]["y"] = vehicle_y
                self.sumo_data[time][vehicle_id]["angle"] = vehicle_angle
                self.sumo_data[time][vehicle_id]["speed"] = vehicle_speed

        # save the data to a file for easy access
        with open("sumo_data.json", "w") as file:
            json.dump(self.sumo_data, file)

    def update_sumo_network(self, time: float):
        """Update the vehicles' locations in the network to the given time based on the SUMO data

        Parameters
        ----------
        time : float
            Time to update the network to

        Returns
        -------
        int
            -1 if the time does not exist in the SUMO data

        """

        # Check if the time exists in the sumo data
        if time not in self.sumo_data:
            print(f"Time {time} does not exist in the SUMO data! Exiting...")
            return -1

        # Update the location of each vehicle
        for vehicle_id in self.sumo_data[time]:
            vehicle = self.sumo_data[time][vehicle_id]
            if vehicle_id not in self.G.nodes:
                self.add_host(Host(vehicle_id, 0, 0, 0, 0))

            self.update_host_location(vehicle_id, vehicle["y"], vehicle["x"])

        # remove the vehicles that are not in the current time
        to_remove = []
        for vehicle_id in self.G.nodes:
            if vehicle_id not in self.sumo_data[time]:
                to_remove.append(vehicle_id)

        for vehicle_id in to_remove:
            self.G.remove_node(vehicle_id)

        self.plot(show_map=True, t=time, plot_labels=False)

    def load_file(self, file_path: str):
        """Initialise network from file

        Parameters
        ----------
        file_path : str
            File path to datacenter file. Must be JSON!

        Raises
        ------
        FileNotFoundError
            If file does not exist
        TypeError
            If file is not JSON
        """

        # Verify if file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError("File not found")
        # Verify if file is JSON
        if not file_path.endswith(".json"):
            raise TypeError("File must be JSON")

        # Load file
        with open(file_path, "r") as file:
            topology_dict = json.load(file)

        self.load_dict(topology_dict)

    def load_dict(self, topology_dict: dict):
        """Initialise from dictionary

        Parameters
        ----------
        topology_dict : dict
            Dictionary containing the network's information.

        Examples
        --------
        >>> topology_dict = {
        ...     "hosts": [
        ...         {"id": 0, "cpu": 2, "ram": 4, "disk": 50, "power": 20},
        ...         {"id": 1, "cpu": 4, "ram": 8, "disk": 100, "power": 80},
        ...         {"id": 2, "cpu": 8, "ram": 16, "disk": 200, "power": 200}
        ...     ],
        ...     "links": [
        ...         {"host_id1": 0, "host_id2": 1, "bandwidth": 50, "delay": 0.05},
        ...         {"host_id1": 1, "host_id2": 2, "bandwidth": 200, "delay": 0.2}
        ...     ]
        ... }
        >>> network = Network()
        >>> network.load_dict(topology_dict)
        >>> network.plot()
        """

        for host in topology_dict["hosts"]:
            self.add_host(Host(**host))

        for link in topology_dict["links"]:
            dist = distance(
                self.get_host(link["host_id1"]).get_location(),
                self.get_host(link["host_id2"]).get_location(),
            ).km
            self.add_link(Link(**link, distance=dist))

    def add_host(self, host: Host):
        """Add host to the network

        Parameters
        ----------
        host : Host
            Host to add to the network
        """

        # print(host)

        self.G.add_node(host.id, host=host)

    def add_link(self, link: Link):
        """Add link to the network

        Parameters
        ----------
        link : Link
            Link to add to the network
        """

        # print(link)

        self.G.add_edge(link.host_id1, link.host_id2, link=link)

    def get_host(self, host_id: int) -> Host:
        """Get host by ID

        Parameters
        ----------
        host_id : int
            ID of the host to get

        Returns
        -------
        Host
            Host with the given ID
        """

        return self.G.nodes[host_id]["host"]

    def update_host_location(
        self,
        host_id: int,
        latitude: float,
        longitude: float,
        altitude: float = -1,
    ):
        """Update the location of a host
        It also updates the link propagation delays.

        Parameters
        ----------
        host_id : int
            ID of the host to update
        latitude : float
            Latitude of the host
        longitude : float
            Longitude of the host
        altitude : float, optional
            Altitude of the host. Default is -1.
            If -1, the altitude will be fetched automatically from the coordinates representing the ground level.
        """

        if altitude == -1:
            # fetch the altitude from the coordinates
            query = f"https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}"
            response = requests.get(query).json()
            altitude = response["results"][0]["elevation"]

        self.get_host(host_id).update_location(latitude, longitude, altitude or 0)

        for adjunted_host in self.G[host_id]:
            link = self.G[host_id][adjunted_host]["link"]
            other_host_location = self.get_host(adjunted_host).get_location()

            flat_distance = distance(  # geopy only accepts lat and lon, no altitude. https://geopy.readthedocs.io/en/stable/#module-geopy.distance
                (latitude, longitude),
                other_host_location[:2],
            ).km
            euclidian_distance = math.sqrt(
                flat_distance**2 + (altitude - other_host_location[2]) ** 2
            )
            link.update_distance(euclidian_distance)

    def plot(self, show_map=False, t=0.0, plot_labels=False):
        """Plot the network

        Parameters
        ----------
        show_map : bool, optional
            Show the map in the background, by default False
        t : float, optional
            Time of the plot, by default 0.0
        plot_labels : bool, optional
            Plot the labels of the nodes, by default False

        """

        # Create node positions
        g = self.G
        pos = {
            n: [g.nodes[n]["host"].longitude, g.nodes[n]["host"].latitude]
            for n in g.nodes
        }
        # print(pos)

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_axis_off()

        # set limits
        ax.set_xlim(self.minlon, self.maxlon)
        ax.set_ylim(self.minlat, self.maxlat)

        if show_map:
            # get latitudes and longitudes from the nodes
            lons = [pos[node][0] for node in pos]
            lats = [pos[node][1] for node in pos]

            nodes = geopandas.GeoDataFrame(
                {
                    "id": list(pos.keys()),
                    "geometry": geopandas.points_from_xy(lons, lats, crs="EPSG:4326"),
                }
            )

            # print(nodes)
            nodes.plot(ax=ax, color="red", markersize=10)

            # Add basemap
            add_basemap(ax, crs="EPSG:4326", attribution_size=5)

        nx.draw_networkx_nodes(g, pos=pos, node_size=10, node_color="red", alpha=0.5)
        nx.draw_networkx_edges(g, pos=pos, edge_color="gray", alpha=0.1)

        plt.tight_layout()

        # TOREMOVE
        plt.savefig(f"./img/img_{t}.png", bbox_inches="tight")
        plt.close()

    def print_hosts(self):
        """Print the hosts of the network"""
        print("Hosts in the network:")
        for host_id in self.G.nodes:
            print(self.get_host(host_id))

    def print_links(self):
        """Print the links of the network"""
        print("Links in the network:")
        for host_id1, host_id2 in self.G.edges:
            print(self.G.edges[host_id1, host_id2]["link"])

    def __str__(self):
        return str(self.G)
