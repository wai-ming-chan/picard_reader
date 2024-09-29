import serial

# Replace '/dev/tty.usbmodemXXXX' with your actual device
ser = serial.Serial('/dev/tty.usbmodem2071368859321', baudrate=115200, timeout=1)

try:
    while True:
        if ser.in_waiting > 0:
            # Read a line of data and decode it
            data = ser.readline().decode('utf-8').strip()
            print(f"Received: {data}")
except KeyboardInterrupt:
    print("Exiting")
finally:
    ser.close()
