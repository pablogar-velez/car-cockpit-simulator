import random
import time

class UART:
    def __init__(self, error_rate=0.1, logger=None):
        self.error_rate = error_rate
        self.logger = logger
        self.buffer = bytes()

    def send(self, data: bytes):
        if random.random() < self.error_rate:
            if self.logger:
                self.logger("[UART] ERROR enviando datos")
            return False
        time.sleep(0.005)
        self.buffer = data
        if self.logger:
            self.logger(f"[UART] Datos enviados: {list(data)}")
        return True

    def receive(self):
        if random.random() < self.error_rate:
            if self.logger:
                self.logger("[UART] ERROR recibiendo datos")
            return None
        if self.logger:
            self.logger(f"[UART] Datos recibidos: {list(self.buffer)}")
        return self.buffer
