import streamlit as st
import pandas as pd
# Load data from public Google Sheet
csv_url = 'https://docs.google.com/spreadsheets/d/16P0fYKSXV8rRGG1oWBmwhY3hkNUXod1rQ60iESQQWCk/edit?usp=sharing'
df = pd.read_csv(csv_url)



# Display the data in Streamlit
st.dataframe(df)

# import streamlit as st
# import pandas as pd
#
# # Load data from public Google Sheet
# csv_url = '../train.csv'
# df = pd.read_csv(csv_url)
#
# # Display the data in Streamlit
# st.dataframe(df)

