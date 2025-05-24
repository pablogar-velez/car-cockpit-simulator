import random

class Bluetooth:
    def __init__(self, error_rate=0.05, logger=print):
        self.connected = True
        self.buffer = []
        self.error_rate = error_rate
        self.logger = logger

    def to_signed_byte(self, value):
        if value < 0:
            return 256 + value
        return value

    def from_signed_byte(self, byte_val):
        if byte_val > 127:
            return byte_val - 256
        return byte_val

    def send(self, data: bytes):
        if not self.connected:
            raise ConnectionError("Bluetooth no está conectado")

        if random.random() < self.error_rate:
            corrupt_index = random.randint(0, len(data)-1)
            corrupted_byte = data[corrupt_index] ^ 0xFF
            corrupted_data = bytearray(data)
            corrupted_data[corrupt_index] = corrupted_byte
            self.buffer.append(bytes(corrupted_data))
            self.logger(f"[Bluetooth] Datos enviados con error: {corrupted_data}")
        else:
            self.buffer.append(data)
            self.logger(f"[Bluetooth] Datos enviados correctamente: {data}")

    def receive(self):
        if not self.buffer:
            return None
        return self.buffer.pop(0)

    def simulate_send_temperature(self, temperature):
        byte_val = self.to_signed_byte(temperature)
        self.send(bytes([byte_val]))

    def simulate_receive_temperature(self):
        data = self.receive()
        if data is None:
            return None
        temp = self.from_signed_byte(data[0])
        return temp