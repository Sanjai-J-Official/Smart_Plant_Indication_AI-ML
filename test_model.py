
from pathlib import Path
import joblib
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_FILE = PROJECT_DIR / "models" / "soil_model.joblib"

model = joblib.load(MODEL_FILE)

test_values = [317, 650, 850]

for value in test_values:
    sample = pd.DataFrame({"raw_value": [value]})
    prediction = model.predict(sample)[0]

    print(f"Sensor value: {value} -> AI prediction: {prediction}")
