# home.py

import streamlit as st


def page_home():
    # Home page content
    # Define the Streamlit app title and a brief description
    st.title("CSVdash - Convert & Visualize CSV Data")
    st.write("Welcome to CSVdash, your tool for converting and visualizing CSV data!")
    st.write(
        "Anime_CSV [link](https://github.com/Otherwa/CSVDash/blob/Otherwa/data/Anime_Analysis.csv)"
    )
    
    st.title("UI Changes:")
    st.write("1. Updated the color scheme for a more modern look.")
    st.write("2. Reorganized the navigation menu for better user flow.")
    st.write("3. Increased font size for improved readability.")

    st.title("User Acceptance Testing (UAT) Progress:")
    st.write("1. Invited stakeholders to test the application.")
    st.write("2. Received feedback on UI and functionality.")
    st.write("3. Identified and fixed several issues reported by users.")
