
import time
from pathlib import Path

import joblib
import pandas as pd
import serial

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_DIR / "models" / "soil_model.joblib"

# Arduino connection settings
PORT = "COM4"
BAUD_RATE = 9600


def main():
    # Load the trained AI model
    if not MODEL_PATH.exists():
        print(f"ERROR: Model not found at {MODEL_PATH}")
        print("Run python python/train_model.py first.")
        return

    model = joblib.load(MODEL_PATH)
    print("AI model loaded.")

    try:
        with serial.Serial(PORT, BAUD_RATE, timeout=2) as arduino:
            # Allow Arduino to restart after serial connection
            time.sleep(2)
            arduino.reset_input_buffer()

            print(f"Connected to Arduino on {PORT}.")
            print("Comparing Arduino and AI predictions...\n")

            while True:
                line = arduino.readline().decode(
                    "utf-8", errors="ignore"
                ).strip()

                # Expected Arduino format: R:306,moist
                if not line.startswith("R:"):
                    continue

                try:
                    sensor_data = line[2:].split(",", 1)

                    if len(sensor_data) != 2:
                        continue

                    raw_value = int(sensor_data[0])
                    arduino_state = sensor_data[1].strip()

                except ValueError:
                    continue

                # Predict using the same feature name as training data
                input_data = pd.DataFrame({
                    "raw_value": [raw_value]
                })

                ai_state = str(model.predict(input_data)[0])

                # Compare Arduino classification with AI prediction
                result = (
                    "MATCH"
                    if arduino_state == ai_state
                    else "MISMATCH"
                )

                print(
                    f"Arduino: {arduino_state:<12} | "
                    f"AI: {ai_state:<12} | {result}"
                )

                # Send AI prediction to Arduino to control outputs
                arduino.write(
                    (ai_state + "\n").encode("utf-8")
                )

    except serial.SerialException as error:
        print(f"\nSerial connection error: {error}")
        print("Check that Arduino is connected to COM4.")
        print("Close the Arduino Serial Monitor before running Python.")

    except KeyboardInterrupt:
        print("\nAI monitoring stopped.")


if __name__ == "__main__":
    main()
