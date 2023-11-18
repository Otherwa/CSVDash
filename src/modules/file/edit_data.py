"""
? edit_csv
++ file.py
"""

import streamlit as st


def edit_data(df):
    # ? Display the DataFrame as a table
    st.write("Table View:")
    df = st.data_editor(df, hide_index=True)
    return df
