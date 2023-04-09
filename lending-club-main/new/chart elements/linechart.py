import streamlit as st
import pandas as pd
import numpy as np

chart_data=pd.DataFrame(
    np.random.rand(25,6),
    columns=['A','B','C','D','E',"F"])

st.line_chart(chart_data )