# sidebar.py

import streamlit as st
from streamlit_option_menu import option_menu


def create_sidebar():
    # Add a sidebar for navigation

    with st.sidebar:
        st.sidebar.title("CSVDash")
        page = st.sidebar.selectbox(
            "Pages:",
            ["Home", "File"],
        )

    # Create a sidebar for file upload and data conversion options
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    return page, uploaded_file
