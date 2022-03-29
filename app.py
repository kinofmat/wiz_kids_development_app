import streamlit as st
import pandas as pd
import numpy as np


locations = pd.read_csv("locations.csv")


top = st.container()

with top:
    st.title("Subway & McDonalds Analysis")

    st.write("Here are all of the Subway and McDonalds locations 4 states: Utah, Colorado, Idaho, and Wyoming")
    st.map(data=locations, zoom=None, use_container_width=True)

