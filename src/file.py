import base64
from datetime import datetime
import streamlit as st


# Custom Dependencies
import pandas as pd
from src.modules.file.chart_gen import generate_charts
from src.modules.file.edit_data import edit_data
from src.modules.file.query import query


# Initialize a variable to store the DataFrame
df = None


def page_file(uploaded_file):
    # Global dataframe
    global df
    if uploaded_file is not None:
        if df is None:
            # Read the uploaded CSV file into a DataFrame
            df = pd.read_csv(uploaded_file, index_col=False)

        # Create a selectbox for switching between tabs
        selected_tab = st.selectbox("Select a tab:", ["Details", "Data", "Query", "Time Details"])

        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if selected_tab == "Details":
            # Generate charts
            generate_charts(df)
        elif selected_tab == "Data":
            # Edit CSV data
            edit_data(df)
        elif selected_tab == "Query":
            query(df)
        elif selected_tab == "Time Details":
            # Display the time the DataFrame was created and the encoding
            st.write(f"DataFrame Created at: {current_time}")

    else:
        st.error("File not uploaded or present")
