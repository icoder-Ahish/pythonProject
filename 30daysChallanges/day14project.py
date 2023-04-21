import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)

############## My Code ##################

# Load a sample dataset
# st.header('`My Streamlit data now showing into dashboard streamlit_pandas_profiling`')
#
# df2 = pd.read_csv("data.csv")
#
# pr2 = df2.profile_report()
# st_profile_report(pr2)
