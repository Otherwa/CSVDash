# sidebar.py

import streamlit as st
from streamlit_option_menu import option_menu


def create_sidebar():
    # Add a sidebar for navigation

    with st.sidebar:
        st.sidebar.title("CSVDash")

        styles = {
            "nav-link": {
                "font-size": "0.9rem",
                "text-align": "left",
                "margin": "0px",
            },
        }

        page = option_menu(
            None,
            ["Home", "File", "Convert Column", "Plot Graph"],
            icons=["house", "cloud-upload", "list-task", "gear"],
            menu_icon="cast",
            default_index=0,
            styles=styles,
        )
        # page = st.sidebar.selectbox(
        #     "Pages:",
        #     ["Home", "File", "Convert Column", "Plot Graph"],
        # )

    # st.sidebar.image(
    #     "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8a97820c-3d54-44c5-bd33-224656c74360/d5a97ie-995eb26b-0e02-4b89-852d-fa1da79edd6b.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhhOTc4MjBjLTNkNTQtNDRjNS1iZDMzLTIyNDY1NmM3NDM2MFwvZDVhOTdpZS05OTVlYjI2Yi0wZTAyLTRiODktODUyZC1mYTFkYTc5ZWRkNmIuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.dReXRU3hJWw4Yr9Uk0RUqt0YnYuveewnjbCQiT9VbNE"
    # )

    # Create a sidebar for file upload and data conversion options
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    return page, uploaded_file
