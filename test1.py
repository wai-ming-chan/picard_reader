import serial
import time

def read_usb_device(port, baud_rate=9600, timeout=1):
    try:
        # Open the serial port with the specified settings
        ser = serial.Serial(port, baudrate=baud_rate, timeout=timeout)
        
        # Enable RTS/CTS or DTR/DSR if needed
        ser.dtr = True  # Enable DTR if required by the device
        ser.rts = True  # Enable RTS if required by the device
        
        time.sleep(2)  # Give the device time to initialize
        
        print(f"Connected to device: {ser.name}")

        # Optional: Send an initialization command to trigger data transmission
        ser.write(b'INIT\n')  # Adjust the command as per your device's protocol
        
        # Reading data in a loop
        while True:
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore').strip()
                if data:
                    print("Data received:", data)
                else:
                    print("Empty data received.")
            else:
                print("No serial data received.")
            time.sleep(0.5)  # Adjust the sleep time as needed

    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    # usb_port = "/dev/tty.usbmodem207136885932"  # Replace with your port
    usb_port = "/dev/tty.usbmodem2071368859321"
    read_usb_device(usb_port)
