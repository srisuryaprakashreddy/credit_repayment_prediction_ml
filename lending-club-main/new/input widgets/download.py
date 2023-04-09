import streamlit as st

import pandas as pd
import numpy as np

sample_text="some thing that will be downloaded ."
# data= pd.DataFrame(np.random.rand(10,5),
#         columns=('a','b','c','d','e'))
st.download_button("Download txt",sample_text)
#  st.download_button("Download dataframe",data = data,mime="data/csv" )
with open("wall.jpg",'rb') as file:
    btn=st.download_button(
        label="Download Image",
        data=file,
        file_name="wall.jpg",
        mime="image/jpg"
    )

@st.cache

def convert_df(df):
    return df.to_csv().encode('utf-8')
df1 = pd.read_csv("cars.csv")
csv = convert_df(df1)

st.download_button(label="Download data as csv ",
                   data=csv,
                   file_name="cars.csv",
                   mime="text/csv " )