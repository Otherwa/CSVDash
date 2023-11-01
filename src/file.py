"""
? file.py
"""
import base64
from datetime import datetime
import streamlit as st

# ? Custom Dependeinces
import pandas as pd
import plotly.express as px
from src.modules.file.chart_gen import generate_charts
from src.modules.file.edit_data import edit_data


# Initialize a variable to store the DataFrame
df = None


from src.modules.file.chart_gen import generate_charts


def get_csv_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="modified_data.csv">Download CSV</a>'
    return href


def page_file(uploaded_file):
    # ? global dataframe
    global df
    if uploaded_file is not None:
        if df is None:
            #  Read the uploaded CSV file into a DataFrame
            df = pd.read_csv(uploaded_file, index_col=False)

        # Create a selectbox for switching between tabs
        selected_tab = st.selectbox("Select a tab:", ["Details", "Data", "Details"])

        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if selected_tab == "Details":
            # * generate charts
            generate_charts(df)
        elif selected_tab == "Data":
            # * edit csv data
            edit_data(df)

        elif selected_tab == "Details":
            # ? Display the time the DataFrame was created and the encoding
            st.write(f"DataFrame Created at: {current_time}")

    else:
        st.error("File not uploaded or present")
