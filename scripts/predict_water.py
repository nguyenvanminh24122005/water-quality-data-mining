import joblib
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "outputs" / "random_forest_model.pkl"

model = joblib.load(MODEL_PATH)

print("Water Potability Predictor")
print("Enter water quality values:")

ph = float(input("pH: "))
hardness = float(input("Hardness: "))
solids = float(input("Solids: "))
chloramines = float(input("Chloramines: "))
sulfate = float(input("Sulfate: "))
conductivity = float(input("Conductivity: "))
organic_carbon = float(input("Organic Carbon: "))
trihalomethanes = float(input("Trihalomethanes: "))
turbidity = float(input("Turbidity: "))

data = np.array([[
    ph,
    hardness,
    solids,
    chloramines,
    sulfate,
    conductivity,
    organic_carbon,
    trihalomethanes,
    turbidity
]])

prediction = model.predict(data)

if prediction[0] == 1:
    print("Water is SAFE to drink")
else:
    print("Water is NOT safe to drink")