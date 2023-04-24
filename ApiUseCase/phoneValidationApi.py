# import requests
#
# response = requests.get(
#     "https://phonevalidation.abstractapi.com/v1/?api_key=afcc2e9609814972bd73edf09c5c8bb8&phone=14152007986")
# print(response.status_code)
# print(response.content)

import requests
import streamlit as st

st.title("Phone Number Validation")

# Get the user input
input_phone = st.text_input("Enter phone number:")

if input_phone:
    # Define API endpoint and parameters
    url = "https://phonevalidation.abstractapi.com/v1/"
    api_key = "afcc2e9609814972bd73edf09c5c8bb8"
    params = {
        "api_key": api_key,
        "phone": input_phone
    }
    # Make API request
    response = requests.get(url, params=params)

    # Check if response was successful
    if response.status_code == 200:
        # Get the validation result from the response
        result = response.json()

        # Display the validation result in Streamlit
        if result["valid"]:
            st.write(f"{input_phone} is a valid phone number!")
        else:
            st.write(f"{input_phone} is not a valid phone number.")
        ########################################3333
        st.write(result.keys())

        # Display the phone number details
        st.write(f"International format: {result['format']}")
        st.write(f"Country prefix: {result['country']}")
        # st.write(f"Country code: {result['country_code']}")
        # st.write(f"Country name: {result['country_name']}")
        st.write(f"Location: {result['location']}")
        st.write(f"Carrier: {result['carrier']}")

    else:
        st.write("Error occurred while validating phone number.")

    # Make API request
    response = requests.get(url, params=params)

    # Check if response was successful
    if response.status_code == 200:
        # Get the validation result from the response
        result = response.json()

        # Display the validation result in Streamlit
        if result["valid"]:
            st.write(f"{input_phone} is a valid phone number!")
        else:
            st.write(f"{input_phone} is not a valid phone number.")
    else:
        st.write("Error occurred while validating phone number.")


# import requests
#
# response = requests.get(
#     "https://emailvalidation.abstractapi.com/v1/?api_key=cf63c80c92c4432aa6aba724140823ef&email=ashishsahu81144@gmail.com")
# print(response.status_code)
# print(response.content)