import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

################################


# Create a sample DataFrame
data = pd.DataFrame({
    'year': [2016, 2017, 2018, 2019, 2020],
    'sales': [100, 150, 200, 250, 300]
})

# Display the line chart
st.line_chart(data['sales'])
