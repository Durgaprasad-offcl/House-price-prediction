import streamlit as st
import joblib

st.title("🏠 House Price Prediction")

st.write("Welcome to my first Machine Learning Web App!")
house_size = st.number_input(
    "Enter House Size (sq ft)",
    min_value=100,
    max_value=10000,
    value=1000
)

st.write("House Size:", house_size)
model = joblib.load("models/house_price_model.pkl")
if st.button("Predict Price"):
    prediction = model.predict([[house_size]])

    st.success(f"🏠 Predicted House Price: ₹{prediction[0]:.2f}")


model = joblib.load("models/house_price_model.pkl")
