import streamlit as st
import joblib
import numpy as np

# load model
model = joblib.load("outputs/random_forest_model.pkl")

st.title("💧 Water Potability Predictor")

st.write("Enter water quality values:")

ph = st.number_input("pH", 0.0, 14.0, 7.0)
hardness = st.number_input("Hardness", 0.0, 500.0, 200.0)
solids = st.number_input("Solids", 0.0, 50000.0, 15000.0)
chloramines = st.number_input("Chloramines", 0.0, 20.0, 7.0)
sulfate = st.number_input("Sulfate", 0.0, 500.0, 300.0)
conductivity = st.number_input("Conductivity", 0.0, 1000.0, 400.0)
organic_carbon = st.number_input("Organic Carbon", 0.0, 30.0, 12.0)
trihalomethanes = st.number_input("Trihalomethanes", 0.0, 150.0, 70.0)
turbidity = st.number_input("Turbidity", 0.0, 10.0, 4.0)

if st.button("Predict"):

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
        st.success("✅ Water is SAFE to drink")
    else:
        st.error("❌ Water is NOT safe to drink")
        