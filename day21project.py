import streamlit as st
import time

st.set_page_config(layout="wide")

st.title('progress bar')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.write("Lodding Completed!! 😄😍😍😍")

st.balloons()