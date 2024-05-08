from simulator.topology import CPU, RAM, Disk, Power

def test_cpu_initialization():
    cpu = CPU()
    assert isinstance(cpu, CPU)

def test_ram_initialization():
    ram = RAM()
    assert isinstance(ram, RAM)

def test_disk_initialization():
    disk = Disk()
    assert isinstance(disk, Disk)

def test_power_initialization():
    power = Power()
    assert isinstance(power, Power)
