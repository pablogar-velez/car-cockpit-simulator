# Car Cockpit Simulator Dashboard

A car cockpit simulator that displays sensor data such as speed, fuel level, oil pressure, temperature, and tire pressure. Each sensor shows its status (OK/ERROR) based on range validations.

The system also simulates communication through CAN, SPI, UART, Bluetooth, and I2C buses, logging messages and statuses in a graphical interface built with Tkinter.

## Features

- Real-time display of simulated sensor data.
- Individual sensor status and overall system health.
- Simulated communication over multiple bus protocols (CAN, SPI, UART, Bluetooth, I2C).
- Message and event logging.
- Simple and thread-safe GUI updates.

## Requirements

- Python 3.7+
- Tkinter (usually included in standard Python installations)
- Custom communication modules: `communication.can_bus`, `communication.spi`, `communication.uart`, `communication.bluetooth`, `communication.i2c`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/car-cockpit-simulator.git
    cd car-cockpit-simulator
    ```

2. Install dependencies (if you have `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python main.py
    ```

## Usage

The application opens a window displaying vehicle indicators and a log area showing messages sent and received over the communication buses.

## Project Structure

