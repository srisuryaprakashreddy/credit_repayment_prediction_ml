import streamlit as st
add_selectbox=st.sidebar.selectbox(
    "how would you like to contact me ",(
    "email","phone","chat")
)

with st.sidebar:
    add_radio=st.radio('choose delivery method',
        ('standard shipping','premimum shipping'))