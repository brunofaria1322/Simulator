from operator import ne
import pytest

from simulator.topology import Network, Host, Link
import networkx as nx
import json


def test_network_initialization():
    network = Network()
    assert isinstance(network.G, nx.Graph)
    assert network.id == 0

    # SUMO
    assert network.sumo_data == {}
    assert network.minlat == 90
    assert network.maxlat == -90
    assert network.minlon == 180
    assert network.maxlon == -180


def test_load_sumo_data():
    network = Network()
    # FileNotFoundError
    with pytest.raises(FileNotFoundError):
        file_path = "file-not-found.xml"
        network.load_sumo_data(file_path)
    # TypeError
    with pytest.raises(TypeError):
        file_path = "file-not-xml.not-xml"
        network.load_sumo_data(file_path)

    # Read from xml file
    file_path = "tests/mobility/sumo/fcd-output-file.xml"
    network.load_sumo_data(file_path)

    assert network.sumo_data == {}
    assert network.minlat == 49.476491
    assert network.maxlat == 49.500569
    assert network.minlon == 8.443093
    assert network.maxlon == 8.512453

    json_output = {}
    expected_json_output = {}
    with open("sumo_data.json", "r") as file:
        json_output = {float(ts): value for (ts, value) in json.load(file).items()}
    with open("tests/mobility/sumo/sumo_data.json", "r") as file:
        expected_json_output = {
            float(ts): value for (ts, value) in json.load(file).items()
        }
    assert json_output == expected_json_output

    # read from json file
    network = Network()
    network.load_sumo_data(file_path)


def test_update_sumo_network():
    network = Network()
    time = 10.0
    network.update_sumo_network(time)
    # Add assertions to check if the sumo network is updated correctly


def test_load_file():
    network = Network()
    file_path = "/path/to/topology_file.json"
    network.load_file(file_path)
    # Add assertions to check if the file is loaded correctly


def test_load_dict():
    network = Network()
    topology_dict = {
        "hosts": [
            {"id": 1, "latitude": 0.0, "longitude": 0.0},
            {"id": 2, "latitude": 1.0, "longitude": 1.0},
        ],
        "links": [
            {"source": 1, "target": 2},
        ],
    }
    network.load_dict(topology_dict)
    # Add assertions to check if the dictionary is loaded correctly


def test_add_host():
    network = Network()
    host = Host(1, 0.0, 0.0)
    network.add_host(host)
    assert network.get_host(1) == host


def test_add_link():
    network = Network()
    link = Link(1, 2)
    network.add_link(link)
    # Add assertions to check if the link is added correctly


def test_update_host_location():
    network = Network()
    host = Host(1, 0.0, 0.0)
    network.add_host(host)
    network.update_host_location(1, 1.0, 1.0)
    updated_host = network.get_host(1)
    assert updated_host.latitude == 1.0
    assert updated_host.longitude == 1.0


def test_plot():
    network = Network()
    network.plot(show_map=False, t=0.0, plot_labels=False)
    # Add assertions to check if the plot is generated correctly


def test_print_hosts():
    network = Network()
    # Add hosts to the network
    network.print_hosts()
    # Add assertions to check if the hosts are printed correctly


def test_print_links():
    network = Network()
    # Add links to the network
    network.print_links()
    # Add assertions to check if the links are printed correctly


def test_str():
    network = Network()
    # Add hosts and links to the network
    network_str = str(network)
    # Add assertions to check if the string representation is correct
