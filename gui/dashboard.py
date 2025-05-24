import tkinter as tk
import random
import threading
import time

from communication.can_bus import CANBus, CANMessage
from communication.spi import SPIBus
from communication.uart import UART
from communication.bluetooth import Bluetooth
from communication.i2c import I2CBus

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Cockpit Simulator Dashboard")

        # Frame para indicadores
        indicators_frame = tk.Frame(root)
        indicators_frame.pack(pady=10)

        # Labels para indicadores
        self.speed_var = tk.StringVar(value="Speed: -- km/h")
        self.speed_status_var = tk.StringVar(value="Speed Sensor Status: --")

        self.fuel_var = tk.StringVar(value="Fuel: -- %")
        self.fuel_status_var = tk.StringVar(value="Fuel Sensor Status: --")

        self.sensor_var = tk.StringVar(value="Overall Sensor Status: --")

        self.oil_var = tk.StringVar(value="Oil Pressure: -- kPa")
        self.oil_status_var = tk.StringVar(value="Oil Pressure Sensor Status: --")

        self.temp_var = tk.StringVar(value="Temperature: -- °C")
        self.temp_status_var = tk.StringVar(value="Temperature Sensor Status: --")

        self.tire_var = tk.StringVar(value="Tire Pressure: -- psi")
        self.tire_status_var = tk.StringVar(value="Tire Pressure Sensor Status: --")

        for var in [self.speed_var, self.speed_status_var,
                    self.fuel_var, self.fuel_status_var,
                    self.oil_var, self.oil_status_var,
                    self.temp_var, self.temp_status_var,
                    self.tire_var, self.tire_status_var,
                    self.sensor_var]:
            label = tk.Label(indicators_frame, textvariable=var, font=("Arial", 12))
            label.pack(anchor="w")

        # Area de logs
        self.log_text = tk.Text(root, height=15, width=100, state=tk.DISABLED)
        self.log_text.pack(pady=10)

        # Crear buses con logger apuntando a self.log()
        self.can = CANBus(error_rate=0.15, logger=self.log)
        self.spi = SPIBus(error_rate=0.15, logger=self.log)
        self.uart = UART(error_rate=0.15, logger=self.log)
        self.bluetooth = Bluetooth(error_rate=0.05, logger=self.log)
        self.i2c = I2CBus(error_rate=0.15, logger=self.log)

        self.running = True
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        threading.Thread(target=self.loop_update, daemon=True).start()

    def log(self, message):
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state=tk.DISABLED)
        print(message)

    def on_close(self):
        self.running = False
        self.root.destroy()

    # Validaciones de sensores
    def validate_speed(self, speed):
        return 0 <= speed <= 240

    def validate_fuel(self, fuel):
        return 0 <= fuel <= 100

    def validate_oil_pressure(self, pressure):
        return 10 <= pressure <= 100  # ejemplo kPa válido

    def validate_temperature(self, temp):
        return -40 <= temp <= 150

    def validate_tire_pressure(self, pressure):
        return 20 <= pressure <= 50  # psi válido

    def loop_update(self):
        while self.running:
            self.simulate_and_update()
            time.sleep(1)

    def simulate_and_update(self):
        # Simular datos sensores
        speed = random.randint(0, 250)
        fuel = random.randint(0, 110)
        oil_pressure = random.randint(5, 110)
        temperature = random.randint(-50, 160)
        tire_pressure = random.randint(15, 55)

        # Validar cada sensor
        speed_status = "OK" if self.validate_speed(speed) else "ERROR"
        fuel_status = "OK" if self.validate_fuel(fuel) else "ERROR"
        oil_status = "OK" if self.validate_oil_pressure(oil_pressure) else "ERROR"
        temp_status = "OK" if self.validate_temperature(temperature) else "ERROR"
        tire_status = "OK" if self.validate_tire_pressure(tire_pressure) else "ERROR"

        # Estado general: si algún sensor está en ERROR, es ERROR
        overall_status = "OK" if all(status == "OK" for status in
                                    [speed_status, fuel_status, oil_status, temp_status, tire_status]) else "ERROR"

        # Actualizar indicadores en GUI (thread-safe)
        self.root.after(0, self.speed_var.set, f"Speed: {speed} km/h")
        self.root.after(0, self.speed_status_var.set, f"Speed Sensor Status: {speed_status}")

        self.root.after(0, self.fuel_var.set, f"Fuel: {fuel} %")
        self.root.after(0, self.fuel_status_var.set, f"Fuel Sensor Status: {fuel_status}")

        self.root.after(0, self.oil_var.set, f"Oil Pressure: {oil_pressure} kPa")
        self.root.after(0, self.oil_status_var.set, f"Oil Pressure Sensor Status: {oil_status}")

        self.root.after(0, self.temp_var.set, f"Temperature: {temperature} °C")
        self.root.after(0, self.temp_status_var.set, f"Temperature Sensor Status: {temp_status}")

        self.root.after(0, self.tire_var.set, f"Tire Pressure: {tire_pressure} psi")
        self.root.after(0, self.tire_status_var.set, f"Tire Pressure Sensor Status: {tire_status}")

        self.root.after(0, self.sensor_var.set, f"Overall Sensor Status: {overall_status}")

        # Simulación de comunicación con buses
        can_msg = CANMessage(0x100, [speed])
        self.can.send(can_msg)
        _ = self.can.receive()

        self.spi.send(bytes([fuel]))
        _ = self.spi.receive()

        self.uart.send(bytes([oil_pressure]))
        _ = self.uart.receive()

        self.bluetooth.simulate_send_temperature(temperature)
        _ = self.bluetooth.receive()

        self.i2c.send(0x52, bytes([tire_pressure]))
        _ = self.i2c.receive()

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
