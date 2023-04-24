import streamlit as st

# Store the user input in session state
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = {}

user_input = st.text_input('Enter some text')
st.session_state['user_input']['text_input'] = user_input

# Retrieve the user input from session state
if 'user_input' in st.session_state:
    text_input = st.session_state.user_input['text_input']
    st.write(f'You entered: {text_input}')

##################################

import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)