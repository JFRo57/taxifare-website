import streamlit as st
import requests

# Título principal
st.title("TaxiFareModel front")

# Descripción
st.markdown("""
# This is a simple Streamlit app to predict taxi fares using the TaxiFareModel API

Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions.
""")

# Inputs del usuario
st.header("Enter your ride details:")

pickup_date = st.date_input("Pickup date")
pickup_time = st.time_input("Pickup time")

pickup_datetime = f"{pickup_date} {pickup_time}"

pickup_longitude = st.number_input("Pickup Longitude", value=40.7614327)
pickup_latitude = st.number_input("Pickup Latitude", value=-73.9798156)
dropoff_longitude = st.number_input("Dropoff Longitude", value=40.6513111)
dropoff_latitude = st.number_input("Dropoff Latitude", value=-73.8803331)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

# Botón para enviar datos
if st.button("Predict fare"):
    url = 'https://taxifare.lewagon.ai/predict'

    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json()["fare"]
        st.success(f"Predicted fare: ${prediction:.2f}")
    else:
        st.error("API request failed. Please try again.")
