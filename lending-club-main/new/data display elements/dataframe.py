import streamlit as st
import pandas as pd
import numpy as np

st.title("dataframe in streamlit")
st.write("""Streamlit is a popular open-source Python library that allows developers to create interactive web applications for data science and machine learning. One of the most common tasks in data science is working with tabular data structures such as Pandas DataFrames. Streamlit provides several ways to display these data structures in an interactive and user-friendly way.

The most common way to display a Pandas DataFrame in Streamlit is by using the st.dataframe() function1. This function displays a DataFrame as an interactive table with features such as column sorting, column resizing, table resizing and search1. You can also use the st.table() function to display a static table2.

Streamlit also provides an experimental data editor called st.experimental_data_editor() which allows users to edit data directly in the table1. This feature is still under development and may change in future versions of Streamlit.

In conclusion, Streamlit provides several ways to display tabular data structures such as Pandas DataFrames in an interactive and user-friendly way. The st.dataframe() function is the most common way to display a DataFrame as an interactive table with features such as column sorting, column resizing, table resizing and search. The st.table() function can be used to display a static table. The experimental data editor called st.experimental_data_editor() allows users to edit data directly in the table.""")
st.markdown("code:-")

st.code("""df = pd.DataFrame(

    np.random.rand(50,20),
    columns =('col %d'%i for i in range(20))
)
st.dataframe(df)""")

st.write("Output")

df = pd.DataFrame(

    np.random.rand(50,20),
    columns =('col %d'%i for i in range(20))
)
st.dataframe(df)