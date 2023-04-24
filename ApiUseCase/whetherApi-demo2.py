import streamlit as st
import requests

# Set page layout
st.set_page_config(page_title="Current Weather", page_icon=":partly_sunny:")

# Define API parameters
url = "https://weatherapi-com.p.rapidapi.com/current.json"
querystring = {"q":"Satna, India"}

# Define API headers
headers = {
    "X-RapidAPI-Key": "9b1ceb7cf2msh9df58c1434776cep1bcbabjsnf62c5c60448e",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

# Make API request
response = requests.request("GET", url, headers=headers, params=querystring)

# Get the weather data from the response
weather_data = response.json()["current"]

# Define CSS styles
st.markdown("""
<style>
h1 {
    font-size: 48px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 20px;
    text-align: center;
}

h2 {
    font-size: 36px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 20px;
    text-align: center;
}

h3 {
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: center;
}

p {
    font-size: 20px;
    margin-top: 10px;
    margin-bottom: 10px;
    text-align: center;
}

img {
    display: block;
    margin: auto;
    margin-top: 30px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# Display the weather data in Streamlit
st.title(":partly_sunny: Current Weather of Satna")
st.image("https://cdn.weatherapi.com/weather/64x64/day/116.png", caption="Satna")


st.write("<h2>Satna, India</h2>", unsafe_allow_html=True)
st.write("<h3>Temperature: {}°C</h3>".format(weather_data["temp_c"]), unsafe_allow_html=True)
st.write("<p>Feels like: {}°C</p>".format(weather_data["feelslike_c"]), unsafe_allow_html=True)
st.write("<p>Wind speed: {} kph</p>".format(weather_data["wind_kph"]), unsafe_allow_html=True)
