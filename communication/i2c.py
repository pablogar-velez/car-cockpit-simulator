import random
import time

class I2CBus:
    def __init__(self, error_rate=0.1, logger=None):
        self.error_rate = error_rate
        self.logger = logger
        self.device_address = None
        self.buffer = bytes()

    def send(self, device_address: int, data: bytes):
        if random.random() < self.error_rate:
            if self.logger:
                self.logger(f"[I2C] ERROR enviando datos al dispositivo {device_address}")
            return False
        time.sleep(0.005)
        self.device_address = device_address
        self.buffer = data
        if self.logger:
            self.logger(f"[I2C] Datos enviados al dispositivo {device_address}: {list(data)}")
        return True

    def receive(self):
        if random.random() < self.error_rate:
            if self.logger:
                self.logger(f"[I2C] ERROR recibiendo datos del dispositivo {self.device_address}")
            return None
        if self.logger:
            self.logger(f"[I2C] Datos recibidos del dispositivo {self.device_address}: {list(self.buffer)}")
        return self.buffer
