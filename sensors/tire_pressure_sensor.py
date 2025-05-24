from communication.bluetooth import BluetoothDevice
import random

bt_device = BluetoothDevice(name="TireSensor")

def read_tire_pressure():
    value = random.randint(30, 40)
    bt_device.send(f"Pressure:{value}")
    received = bt_device.receive()
    return int(received.split(":")[1]) if received else value
