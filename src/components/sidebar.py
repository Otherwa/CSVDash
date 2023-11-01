# sidebar.py

import streamlit as st


def create_sidebar():
    # Add a sidebar for navigation
    st.sidebar.title("CSVDash")
    page = st.sidebar.selectbox(
        "Pages:",
        ["Home", "File", "Convert Column", "Plot Graph"],
    )

    # st.sidebar.image(
    #     "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8a97820c-3d54-44c5-bd33-224656c74360/d5a97ie-995eb26b-0e02-4b89-852d-fa1da79edd6b.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhhOTc4MjBjLTNkNTQtNDRjNS1iZDMzLTIyNDY1NmM3NDM2MFwvZDVhOTdpZS05OTVlYjI2Yi0wZTAyLTRiODktODUyZC1mYTFkYTc5ZWRkNmIuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.dReXRU3hJWw4Yr9Uk0RUqt0YnYuveewnjbCQiT9VbNE"
    # )

    # Create a sidebar for file upload and data conversion options
    st.sidebar.header("Upload CSV File")
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    st.sidebar.write("Upload your CSV file on the left sidebar to get started.")

    return page, uploaded_file
