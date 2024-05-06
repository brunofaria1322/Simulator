from simulator.topology import Host


def test_host_creation():
    host = Host(0, 2, 4, 50, 20)
    assert host.id == 0
    assert host.cpu == 2
    assert host.ram == 4
    assert host.disk == 50
    assert host.power == 20
    assert host.latitude == 0
    assert host.longitude == 0
    assert host.altitude == 0

def test_host_creation_with_optional_parameters():
    host = Host(0, 2, 4, 50, 20, 40.186476, -8.4157114, 100)
    assert host.id == 0
    assert host.cpu == 2
    assert host.ram == 4
    assert host.disk == 50
    assert host.power == 20
    assert host.latitude == 40.186476
    assert host.longitude == -8.4157114
    assert host.altitude == 100


def test_host_location():
    host = Host(0, 2, 4, 50, 20, 40.186476, -8.4157114)
    assert host.get_location() == (40.186476, -8.4157114, 0)


def test_update_location():
    host = Host(0, 2, 4, 50, 20)
    host.update_location(40.186476, -8.4157114, 0)
    assert host.get_location() == (40.186476, -8.4157114, 0)


def test_task_allocation():
    # TODO: Implement this test
    pass


def test_task_release():
    # TODO: Implement this test
    pass


def test_host_str():
    host = Host(0, 2, 4, 50, 20)
    assert str(host) == "Host 0: CPU = 2 IPS, RAM = 4 GB, Disk = 50 GB, Power = 20 W"
    # with location
    host = Host(0, 2, 4, 50, 20, 40.186476, -8.4157114)
    print(str(host))
    assert (
        str(host)
        == "Host 0: CPU = 2 IPS, RAM = 4 GB, Disk = 50 GB, Power = 20 W, Location = (40.186476, -8.4157114, 0)"
    )
    # with location and altitude
    host = Host(0, 2, 4, 50, 20, 40.186476, -8.4157114, 100)
    assert (
        str(host)
        == "Host 0: CPU = 2 IPS, RAM = 4 GB, Disk = 50 GB, Power = 20 W, Location = (40.186476, -8.4157114, 100)"
    )
