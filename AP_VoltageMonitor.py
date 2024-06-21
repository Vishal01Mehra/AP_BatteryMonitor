import time
from pymavlink import mavutil
from playsound import playsound

def connect_to_drone(connection_string):
    # Connect to the drone
    master = mavutil.mavlink_connection(connection_string)
    # Wait for the first heartbeat to ensure connection is established
    master.wait_heartbeat()
    print("Heartbeat received from the drone.")
    return master

def monitor_battery(master):
    while True:
        # Wait for a BATTERY_STATUS message
        msg = master.recv_match(type='BATTERY_STATUS', blocking=True)
        if not msg:
            continue

        # Extract the battery voltage (in millivolts)
        voltage_battery = msg.voltages[0] / 1000.0  # Convert to volts
        
        print(f"Battery voltage: {voltage_battery:.2f} V")

        # Check if the voltage is lower than 50 volts
        if voltage_battery < 50.0:
            print("Warning: Battery voltage is below 50 volts!")
            playsound('alert.mp3')

        # Sleep for a short duration to reduce CPU usage
        time.sleep(1)

def main():
    # Connection string for the drone
    # For example, if connecting via UDP, it might look like: 'udp:127.0.0.1:14550'
    connection_string = 'udp:127.0.0.1:14550'

    try:
        master = connect_to_drone(connection_string)
        monitor_battery(master)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
