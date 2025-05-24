from communication.spi import SPIMaster, SPIDevice

spi_master = SPIMaster(clock_speed_hz=500000)
spi_slave = SPIDevice(name="OilSensor")
spi_master.connect_device(spi_slave)

def read_oil_pressure():
    command = 0b10101010
    response = spi_master.transfer_byte(command)
    return response
