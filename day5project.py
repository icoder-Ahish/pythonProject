import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Day5Project')



st.write('In This project we created the pandas datafram and use the with altr to visualize ')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

####################################
csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

# If a file was uploaded
if csv_file is not None:
    df3 = pd.read_csv(csv_file)
    chart = alt.Chart(df3).mark_point().encode(
         x='Index',
         y='User Id',
         color='Sex',
         tooltip=['Index', 'User Id', 'Sex']
    ).interactive()
    st.write(chart)
##################################