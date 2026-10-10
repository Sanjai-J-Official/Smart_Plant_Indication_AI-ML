
import serial
import time

PORT = "COM4"
BAUD_RATE = 9600

try:
    with serial.Serial(PORT, BAUD_RATE, timeout=2) as arduino:
        time.sleep(2)

        print("Connected to Arduino!")
        print("Reading live sensor data. Press Ctrl+C to stop.\n")

        while True:
            line = arduino.readline().decode(
                "utf-8", errors="ignore"
            ).strip()

            if line:
                print("Sensor reading:", line)

except serial.SerialException as error:
    print("Connection error:", error)
    print("Check COM4 and close Arduino Serial Monitor.")

except KeyboardInterrupt:
    print("\nSensor reading stopped.")
