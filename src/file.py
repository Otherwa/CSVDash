# file.py

import streamlit as st
import pandas as pd


def page_file(uploaded_file):
    if uploaded_file is not None:
        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(uploaded_file, index_col=False)
        df.reset_index(drop=True, inplace=True)
        # Display the DataFrame as a table
        st.write("Table View:")
        st.write(df)
    else:
        st.error("File not Upload or Present")
