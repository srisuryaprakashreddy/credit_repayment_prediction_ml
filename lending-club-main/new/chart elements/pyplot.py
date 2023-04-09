import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st 

arr =np.random.normal(1,1,size=100)
arr2 =np.random.normal(3,4,size=100)

data= pd.DataFrame(arr2)

st.dataframe(data)

fig,ax=plt.subplots()

ax.hist(arr,bins=20)

st.pyplot(fig)