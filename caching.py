import streamlit as st
import time

@st.cache_data()
def printer_massage():
    st.write("Running.......")
    time.sleep(4)
    return "Message"

st.write(printer_massage())