from communication.i2c import I2CBus, I2CDevice

i2c_bus = I2CBus()
temp_sensor = I2CDevice(0x48)
i2c_bus.connect_device(temp_sensor)

def read_temperature():
    # Simula lectura del registro 0x00 del sensor
    return i2c_bus.read(0x48, 0x00)
