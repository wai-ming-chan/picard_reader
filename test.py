import serial
import time

def read_usb_device(port, baud_rate=9600, timeout=1):
    try:
        ser = serial.Serial(port, baudrate=baud_rate, timeout=timeout)
        time.sleep(2)  # Give the device time to initialize

        print("Connected to device:", ser.name)

        while True:
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore').strip()
                if data:
                    print("Data received:", data)
                else:
                    print("Empty data received.")
            else:
                print("No serial data received.")
            time.sleep(0.1)

    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    usb_port = "/dev/tty.usbmodem2071368859321"  # Update with your port
    read_usb_device(usb_port)


# import serial
# import time

# def read_usb_device(port, baud_rate=9600, timeout=1):
#     try:
#         # Open the serial port with the specified settings
#         ser = serial.Serial(port, baudrate=baud_rate, timeout=timeout)

#         # Wait for the device to initialize
#         time.sleep(2)  # Adjust this if needed for your device

#         print("Connected to device:", ser.name)

#         # Reading data in a loop
#         while True:
#             if ser.in_waiting > 0:
#                 data = ser.readline().decode('utf-8').strip()  # Read and decode data
#                 print("Data received:", data)

#             time.sleep(0.1)  # Adjust the sleep time as needed

#     except serial.SerialException as e:
#         print(f"Error opening serial port {port}: {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         if 'ser' in locals() and ser.is_open:
#             ser.close()
#             print("Serial port closed.")

# if __name__ == "__main__":
#     # Replace 'COM3' or '/dev/ttyUSB0' with the correct serial port of your device
#     usb_port = "/dev/tty.usbmodem2071368859321"  # or "/dev/ttyUSB0" on Linux/Mac
#     read_usb_device(usb_port)
