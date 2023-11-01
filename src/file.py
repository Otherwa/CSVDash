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


def get_csv_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="modified_data.csv">Download CSV</a>'
    return href


from src.modules.file.chart_gen import generate_charts


def get_csv_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="modified_data.csv">Download CSV</a>'
    return href


def page_file(uploaded_file):
    if uploaded_file is not None:
        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(uploaded_file, index_col=False)

        # Create a selectbox for switching between tabs
        selected_tab = st.selectbox("Select a tab:", ["Details", "Data", "Details"])

        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if selected_tab == "Details":
            # * generate charts
            generate_charts(df)
        elif selected_tab == "Data":
            # ? Display the DataFrame as a table
            st.write("Table View:")
            df = st.data_editor(df, hide_index=True)

            # ? Add a save button
            if st.button("Download CSV"):
                # ? Generate a CSV file with a unique name
                download_link = get_csv_download_link(df)
                st.markdown(download_link, unsafe_allow_html=True)

        elif selected_tab == "Details":
            # ? Display the time the DataFrame was created and the encoding
            st.write(f"DataFrame Created at: {current_time}")

    else:
        st.error("File not uploaded or present")
