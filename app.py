import streamlit as st
import requests
import pandas as pd

# Título principal
st.title("TaxiFareModel front")

# Descripción
st.markdown("""
# This is a simple Streamlit app to predict taxi fares using the TaxiFareModel API
""")

# Inputs del usuario
st.header("Enter your ride details:")

pickup_date = st.date_input("Pickup date")
pickup_time = st.time_input("Pickup time")

pickup_datetime = f"{pickup_date} {pickup_time}"

pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

map_df=pd.DataFrame([
    {"lon":pickup_longitude,"lat":pickup_latitude},
    {"lon":dropoff_longitude,"lat":dropoff_latitude}
  ])
st.map(
    map_df,
    zoom=12,
    use_container_width=True
)

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
