import streamlit as st
import pandas as pd
import numpy as np

chart_data=pd.DataFrame(np.random.randn(20,3),
        columns=('a','b','c'))


col1,col2,col3 =st.columns(3)

with col1:
    st.header("column 1")
    st.title("col1")
    st.write("text under col 1")

with col2:
    st.header("column 2")
    st.area_chart(chart_data)
    st.write("text under col 2")
with col3:
    st.header("column 3")
    st.write("text under col 3")