# Import Streamlit and Pandas
import streamlit as st
import pandas as pd

# Import for API calls
import requests

# Import for navbar
from streamlit_option_menu import option_menu

# Import for dyanmic tagging
from streamlit_tags import st_tags, st_tags_sidebar

# Imports for aggrid
from st_aggrid import AgGrid
from st_aggrid import AgGrid
import pandas as pd
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid import GridUpdateMode, DataReturnMode

# Import for keyboard shortcuts
# from dashboard_utils.gui import keyboard_to_url
# from dashboard_utils.gui import load_keyboard_class
#######################################################
if "widen" not in st.session_state:
    layout = "centered"
else:
    layout = "wide" if st.session_state.widen else "centered"
######################33

st.set_page_config(layout=layout, page_title="Zero-Shot Text Classifier", page_icon="🤗")

#######################3
st.image("logo.png", width=350)

st.title("Zero-Shot Text Classifier")

1, c2 = st.columns([0.4, 2])

with c1:

    st.image(
        "logo.png",
        width=110,
    )

with c2:

    st.caption("")
    st.title("Zero-Shot Text Classifier")


st.sidebar.image(
    "30days_logo.png",
)

st.write("")

st.markdown(
    """
Classify keyphrases fast and on-the-fly with this mighty app. No ML training needed!
Create classifying labels (e.g. `Positive`, `Negative` and `Neutral`), paste your keyphrases, and you're off!  
"""
)

st.write("")

st.sidebar.write("")




with st.sidebar:
    selected = option_menu(
        "",
        ["Demo", "Unlocked Mode"],
        icons=["bi-joystick", "bi-key-fill"],
        menu_icon="",
        default_index=0,
    )
