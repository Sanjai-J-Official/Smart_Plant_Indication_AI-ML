
from pathlib import Path

import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Find the project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "soil_data.csv"
MODEL_DIR = PROJECT_DIR / "models"
MODEL_FILE = MODEL_DIR / "soil_model.joblib"

# Load the sample dataset
data = pd.read_csv(DATA_FILE)

X = data[["raw_value"]]
y = data["state"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)

print("Model training completed!")
print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
print("\nClassification report:")
print(classification_report(y_test, predictions, zero_division=0))

# Save the trained model
MODEL_DIR.mkdir(parents=True, exist_ok=True)
joblib.dump(model, MODEL_FILE)

print(f"\nModel saved to: {MODEL_FILE}")
