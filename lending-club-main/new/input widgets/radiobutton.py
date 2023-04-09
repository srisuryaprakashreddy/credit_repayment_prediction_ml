import streamlit as st

genre =st.radio(
    "what's your favorite genre",
    ('Comedy','action','drama')
)

if genre == "Comedy" :
    st.write("yoyu selected comedy")
else:
    st.write("you did not select comedy")
