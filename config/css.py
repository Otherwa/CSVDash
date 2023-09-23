import streamlit as st
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
custom_css_path = os.path.join(current_directory, "custom.css")


def load_custom_css():
    with open(custom_css_path, "r") as f:
        # Create the menu box
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
