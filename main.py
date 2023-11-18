# Custom dependencies
from config.css import load_custom_css
from src.components.sidebar import create_sidebar

# pages
from src.file import page_file
from src.home import page_home

# Dependencies
import streamlit as st
import pandas as pd
import base64


def main():
    # Config
    load_custom_css()
    st.set_option("deprecation.showfileUploaderEncoding", False)

    # Create sidebar and get page and uploaded file
    page, uploaded_file = create_sidebar()

    if page == "Home":
        page_home()
    elif page == "File":
        page_file(uploaded_file)


if __name__ == "__main__":
    st.set_option("deprecation.showfileUploaderEncoding", False)
    st.set_page_config(
        page_title="CSVDash",
        page_icon=":chart_with_upwards_trend:",
    )

    main()
