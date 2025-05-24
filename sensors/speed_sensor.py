from communication.can_bus import CANBus, CANMessage
import random

can_bus = CANBus()

def read_speed():
    speed = random.randint(0, 240)
    msg = CANMessage(0x100, [speed])
    can_bus.send(msg)
    # Simulamos lectura inmediata para demo
    received = can_bus.receive()
    return received.data[0] if received else speed
