# First, we will need the following imports for our application.

import json
import streamlit as st
from pathlib import Path

# As for Streamlit Elements, we will need all these objects.
# All available objects and there usage are listed there: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# Change page layout to make the dashboard take the whole page.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # Define URL for media player.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")



if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()


layout = [
    # Editor item is positioned in coordinates x=0 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("editor", 0, 0, 6, 3),
    # Chart item is positioned in coordinates x=6 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("chart", 6, 0, 6, 3),
    # Media item is positioned in coordinates x=0 and y=3, and takes 6/12 columns and has a height of 4.
    dashboard.Item("media", 0, 2, 12, 4),
]

# Create a frame to display elements.

with elements("demo"):

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # To make this header draggable, we just need to set its classname to 'draggable',
            # as defined above in dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Editor", className="draggable")


            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                mui.Button("Apply changes", onClick=sync())


        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            mui.CardHeader(title="Chart", className="draggable")


            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={ "scheme": "spectral" },
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={ "theme": "background" },
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={ "from": "serie.color" },
                    axisTop={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": -36
                    },
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
                    axisRight=None,
                )

        # Third element of the dashboard, the Media player.

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # This element is powered by ReactPlayer, it supports many more players other
                # than YouTube. You can check it out there: https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)