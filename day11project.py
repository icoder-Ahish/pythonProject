import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

###############3
import streamlit as st

# Define a dictionary of options
options = {
    'Ram': 'Student',
    'Ashish': 'Teacher',
    'Rohan': 'Developer',
    'Rohit': 'Manager',
}

# Display the multi-select dropdown menu
selected_options = st.multiselect('Select one or more options', list(options.keys()))

# Get the values corresponding to the selected options
selected_values = [options[key] for key in selected_options]

# Print the selected options and values
st.write('You selected:', selected_options)
st.write('The corresponding values are:', selected_values)

