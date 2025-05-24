from communication.uart import UARTSim
import random

uart = UARTSim()

def read_fuel_level():
    value = random.randint(0, 100)
    uart.send_byte(value)
    uart.receive_byte(value)  # Simula eco
    return value
