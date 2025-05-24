import random
import time

class CANMessage:
    def __init__(self, id_, data):
        self.id = id_
        self.data = data

class CANBus:
    def __init__(self, error_rate=0.1, logger=None):
        self.error_rate = error_rate
        self.logger = logger
        self.buffer = []

    def send(self, msg: CANMessage):
        # Simular posible error
        if random.random() < self.error_rate:
            if self.logger:
                self.logger(f"[CANBus] ERROR enviando mensaje ID {msg.id}")
            return False
        # Simular tiempo de envío
        time.sleep(0.01)
        self.buffer.append(msg)
        if self.logger:
            self.logger(f"[CANBus] Mensaje enviado ID {msg.id} Data: {msg.data}")
        return True

    def receive(self):
        # Simular posible error
        if not self.buffer:
            return None
        if random.random() < self.error_rate:
            if self.logger:
                self.logger("[CANBus] ERROR recibiendo mensaje")
            return None
        msg = self.buffer.pop(0)
        if self.logger:
            self.logger(f"[CANBus] Mensaje recibido ID {msg.id} Data: {msg.data}")
        return msg
