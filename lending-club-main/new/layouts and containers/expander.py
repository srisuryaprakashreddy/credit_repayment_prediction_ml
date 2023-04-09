import streamlit as st

st.bar_chart({"data":[1,2,4,1,5,7,6]})

with st.expander("Expand me to see some text "):
    st.write("some text ")
    st.write("""A bar chart or bar graph is a 
    chart or graph that presents categorical
     data with rectangular bars with heights 
     or lengths proportional to the values tha
     they represent. The bars can be plotted 
     vertically or horizontally. In addition, 
     in a simple bar chart or graph, we make bars 
     of equal width but their length varies according
    to the data.""")