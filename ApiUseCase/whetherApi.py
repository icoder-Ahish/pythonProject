import streamlit as st
import requests

st.title("Current Weather")

# Define API parameters
url = "https://weatherapi-com.p.rapidapi.com/current.json"
querystring = {"q":"London, UK"}

# Define API headers
headers = {
    "X-RapidAPI-Key": "9b1ceb7cf2msh9df58c1434776cep1bcbabjsnf62c5c60448e",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

# Make API request
response = requests.request("GET", url, headers=headers, params=querystring)

# Get the weather data from the response
weather_data = response.json()["current"]

# Display the weather data in Streamlit
st.write("Temperature:", weather_data["temp_c"], "°C")
st.write("Feels like:", weather_data["feelslike_c"], "°C")
st.write("Wind speed:", weather_data["wind_kph"], "kph")
