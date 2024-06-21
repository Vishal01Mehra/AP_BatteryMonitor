# ArduPilot Battery Monitor

This project provides a Python script to monitor the battery voltage of an ArduPilot drone over the network. If the battery voltage drops below 50 volts, the script will print a warning message and play an audio alert.

## Prerequisites

- Python 3.x
- `pymavlink` library
- `playsound` library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Vishal01Mehra/AP_BatteryMonitor.git
    cd AP_BatteryMonitor
    ```

2. **Install required Python packages**:
    ```bash
    pip install pymavlink playsound
    ```

3. **Add an audio alert file**:
   Place an audio file named `alert.mp3` in the same directory as `monitor_battery.py`.

## Usage

1. **Edit the connection string** in `monitor_battery.py` to match your drone's connection details. The connection string might look like:
    - For UDP: `udp:127.0.0.1:14550`
    - For TCP: `tcp:127.0.0.1:5760`
    - For Serial: `com14` or `/dev/ttyUSB0`

2. **Run the script**:
    ```bash
    python monitor_battery.py
    ```

## Example

```bash
Heartbeat received from the drone.
Battery voltage: 51.23 V
Battery voltage: 51.20 V
Warning: Battery voltage is below 50 volts!
