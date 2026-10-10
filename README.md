# 🌱 Smart Plant Moisture Alert Using Arduino and AI/ML

An Arduino-based smart plant monitoring project that reads soil moisture sensor values, classifies moisture conditions using a Machine Learning model, compares Arduino and AI predictions, and controls LED and buzzer alerts.

## 📌 Project Overview

Plants require suitable soil moisture for healthy growth. This project monitors soil moisture using an Arduino-compatible sensor and uses a Python-based Machine Learning model to predict the soil condition.

The system compares the Arduino's threshold-based classification with the AI model's prediction and displays the result in the terminal.

## ✨ Features

- 🌱 Real-time soil moisture sensor readings
- 🤖 Machine Learning-based moisture classification
- 🔄 Arduino and Python serial communication
- 📊 Side-by-side comparison of Arduino and AI predictions
- ✅ `MATCH` and `MISMATCH` status display
- 💡 LED alerts based on predicted moisture conditions
- 🔔 Buzzer alert for critical dry conditions
- 🐍 Python-based model training and prediction

## 🛠️ Technologies Used

- Arduino UNO
- Soil moisture sensor
- Python
- Pandas
- Scikit-learn
- Joblib
- PySerial
- Arduino IDE
- Visual Studio Code

## 🧰 Hardware Components

- Arduino UNO board
- Soil moisture sensor
- LEDs connected to the existing circuit
- Buzzer
- Breadboard and jumper wires
- USB cable

## 🔌 Pin Configuration

| Component | Arduino Pin |
|---|---|
| Soil moisture sensor analog output | A0 |
| Green LED output | D8 |
| Red LED output | D9 |
| Buzzer | D10 |

**Note:** The pin names in the code refer to logical outputs. Verify the physical LED colors and wiring against your actual circuit.

## 📁 Project Structure

```text
SmartPlant-AI-ML/
│
├── arduino/
│   └── SmartPlant_AI.ino
│
├── data/
│   └── soil_data.csv
│
├── models/
│   └── soil_model.joblib
│
├── python/
│   ├── live_ai_monitor.py
│   ├── read_sensor.py
│   ├── test_model.py
│   └── train_model.py
│
└── README.md
```

## ⚙️ How It Works

1. The soil moisture sensor provides an analog reading to the Arduino.
2. The Arduino converts the reading into a moisture state using predefined thresholds.
3. The Arduino sends the sensor value and state to Python through serial communication.
4. Python loads the trained Machine Learning model and predicts the moisture condition.
5. Python compares the Arduino state with the AI prediction.
6. The terminal displays `MATCH` when both classifications agree and `MISMATCH` when they differ.
7. Python sends the AI prediction back to the Arduino to control the existing LED and buzzer outputs.

## 🧠 Moisture Classification

The project uses three classification labels:

| State | Description |
|---|---|
| `moist` | Soil reading is below the dry threshold |
| `dry` | Soil reading reaches the dry threshold |
| `critical_dry` | Soil reading reaches the critical threshold |

The current Arduino example uses these provisional thresholds:

- Dry threshold: `700`
- Critical dry threshold: `820`

These values should be calibrated using actual readings from the sensor and the soil conditions being tested.

## 🐍 Python Environment Setup

### 1. Install Python

Install Python on your computer and ensure it is available from the terminal.

### 2. Install dependencies

Open a terminal in the project directory and run:

```bash
python -m pip install pandas scikit-learn joblib pyserial
```

### 3. Train the Machine Learning model

Run:

```bash
python python/train_model.py
```

This script trains the classifier using `data/soil_data.csv` and saves the model in the `models/` directory.

### 4. Test the model

Run:

```bash
python python/test_model.py
```

### 5. Upload the Arduino code

1. Open `arduino/SmartPlant_AI.ino` in Arduino IDE.
2. Select the Arduino UNO board.
3. Select the correct serial port.
4. Verify and upload the code.

### 6. Run the live AI monitor

Close the Arduino IDE Serial Monitor and run:

```bash
python python/live_ai_monitor.py
```

Ensure that the COM port and baud rate in the Python script match the Arduino connection.

## 📊 Sample Terminal Output

```text
AI model loaded.
Connected to Arduino on COM4.
Comparing Arduino and AI predictions...

Arduino: moist        | AI: moist        | MATCH
Arduino: dry          | AI: dry          | MATCH
Arduino: critical_dry | AI: critical_dry | MATCH
```

*The output above is illustrative. Actual readings and predictions depend on the sensor, trained model, and soil conditions.*

## ⚠️ Important Notes

- The initial dataset contains sample values and labels. Predictions have not been independently validated against a large set of real sensor readings.
- A `MATCH` means the Arduino classification and AI prediction agree; it does not prove that either classification is correct.
- Sensor readings vary with the sensor type, soil composition, moisture level, and wiring.
- Calibrate the thresholds and evaluate the model using representative, labelled sensor measurements before relying on it for plant care.
- Keep the Arduino Serial Monitor closed while the Python monitor is using the same serial port.
- The current circuit code independently controls two LED outputs and one buzzer.

## 🚀 Future Improvements

- Collect a larger real-world soil moisture dataset.
- Improve model evaluation using representative labelled measurements.
- Add sensor calibration and configurable thresholds.
- Develop a graphical dashboard for live monitoring.
- Store sensor readings for analysis and visualization.
- Explore remote monitoring and IoT integration.

## 🎯 Applications

- Smart gardening
- Indoor plant monitoring
- Soil moisture demonstrations
- Educational Arduino and Machine Learning projects
- Introductory smart agriculture systems

## 👨‍💻 Author

**Sanjai J**

Developed as an educational project combining Arduino, Python, and Machine Learning.

## 📄 License

This project is available for educational and learning purposes. Add a `LICENSE` file if you want to specify formal reuse and distribution terms.
