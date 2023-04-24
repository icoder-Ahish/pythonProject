import streamlit as st
import requests

st.title("Current Weather")

# Get location input from user
location = st.text_input("Enter a location:")
Country = st.text_input("Enter Country Name:")

if location and Country:
    # Define API parameters
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": location + "," + Country}

    # Define API headers
    headers = {
        "X-RapidAPI-Key": "9b1ceb7cf2msh9df58c1434776cep1bcbabjsnf62c5c60448e",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
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

    # Make API request
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Get the weather data from the response
    if response.ok:
        weather_data = response.json()["current"]

        # Display the weather data in Streamlit

        st.title(f":partly_sunny: Current Weather of {location}")
        st.image("https://cdn.weatherapi.com/weather/64x64/day/116.png", caption="Weather in " + location)

        st.write(f"<h2> {location}, {Country}</h2>", unsafe_allow_html=True)
        st.write("<h3>Temperature: {}°C</h3>".format(weather_data["temp_c"]), unsafe_allow_html=True)
        st.write("<p>Feels like: {}°C</p>".format(weather_data["feelslike_c"]), unsafe_allow_html=True)
        st.write("<p>Wind speed: {} kph</p>".format(weather_data["wind_kph"]), unsafe_allow_html=True)
    else:
        st.write("Failed to retrieve weather data for the specified location.")
