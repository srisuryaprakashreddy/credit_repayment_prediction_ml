import streamlit as st
from datetime import time
from datetime import datetime

age=st.slider("how old are you",0,130,25)
st.write("i am",age,"years old")

values = st.slider('select a range of values' ,
                   0.0,100.0,(25.0,75.0))
st.write("Values :",values)

appointment =st.slider("schedule your appointment :",
                       value=(time(11,30),time(12,45)))
st.write("you're scheduled for:",appointment)

start_time =st.slider("when do you start",
                      value=datetime(2023,3,1,9,30),
                      format="'MM/DD/YY - hh:mm")
st.write("start time :",start_time)