import streamlit as st
import datetime

date=st.date_input("when is your birthday ?",
                   datetime.date(2019,7,6))

st.write("your birthday is :",date)