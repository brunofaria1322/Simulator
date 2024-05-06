from simulator.topology import Link


def test_link_initialization():
    link = Link(100, 10.5)
    assert link.bandwidth == 100
    assert link.distance == 10.5
    assert link.packet_loss_rate == 0
    assert link.is_wired is True


def test_link_initialization_with_optional_parameters():
    link = Link(100, 10.5, 0.1, False)
    assert link.bandwidth == 100
    assert link.distance == 10.5
    assert link.packet_loss_rate == 0.1
    assert link.is_wired is False


def test_update_distance():
    link = Link(100, 10.5)
    link.update_distance(15.2)
    assert link.distance == 15.2


def test_transfer_data():
    # TODO: Implement this test
    pass


def test_is_available():
    link = Link(100, 10.5)
    assert link.is_available(50) is True
    assert link.is_available(150) is False


def test_str():
    link = Link(100, 10.5)
    print(str(link))
    assert (
        str(link)
        == "Bandwidth = 100 Mbps, Distance = 10.5 km, Packet Loss Rate = 0 %, is_wired = True"
    )
