# sidebar.py

import streamlit as st
from streamlit_option_menu import option_menu


def create_sidebar():
    # Add a sidebar for navigation

    with st.sidebar:
        st.sidebar.title("CSVDash")

        # styles = {
        #     "nav-link": {
        #         "font-size": "0.9rem",
        #         "text-align": "left",
        #         "margin": "0px",
        #     },
        # }

        # page = option_menu(
        #     None,
        #     ["Home", "File", "Convert Column", "Plot Graph"],
        #     icons=["house", "cloud-upload", "list-task", "gear"],
        #     menu_icon="cast",
        #     default_index=0,
        #     styles=styles,
        # )
        st.sidebar.image(
            "https://i.pinimg.com/originals/80/7b/5c/807b5c4b02e765bb4930b7c66662ef4b.gif",
            width=100,
        )
        page = st.sidebar.selectbox(
            "Pages:",
            ["Home", "File"],
        )

    # Create a sidebar for file upload and data conversion options
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    return page, uploaded_file
