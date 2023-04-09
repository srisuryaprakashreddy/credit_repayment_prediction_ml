import streamlit as st
import pandas as pd
import numpy as np

chart_data=pd.DataFrame(np.random.randn(20,4,)
        ,columns=('a','b','c','d'))
st.header("Chart elements in StreamLit \n \n ")
st.subheader("barchart :-")
st.bar_chart(chart_data)
st.subheader("areachart :-")
st.area_chart(chart_data)
st.subheader("linechart :-")
st.line_chart(chart_data)