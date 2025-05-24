import random
import time

class SPIBus:
    def __init__(self, error_rate=0.1, logger=None):
        self.error_rate = error_rate
        self.logger = logger
        self.buffer = bytes()

    def send(self, data: bytes):
        if random.random() < self.error_rate:
            if self.logger:
                self.logger("[SPI] ERROR enviando datos")
            return False
        time.sleep(0.005)
        self.buffer = data
        if self.logger:
            self.logger(f"[SPI] Datos enviados: {list(data)}")
        return True

    def receive(self):
        if random.random() < self.error_rate:
            if self.logger:
                self.logger("[SPI] ERROR recibiendo datos")
            return None
        if self.logger:
            self.logger(f"[SPI] Datos recibidos: {list(self.buffer)}")
        return self.buffer
