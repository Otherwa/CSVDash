import streamlit as st
import pandas as pd
import requests

def query_csv_with_huggingface_api(df):
    # Display a text box for the user to input the question
    question = st.text_input("Enter your question:")

    # Check if a question is provided
    if not question:
        st.warning("Please enter a question.")
        return

    # Display the question and the DataFrame
    st.subheader(f"Query the DataFrame with Question: '{question}'")
    st.dataframe(df, height=300)
    
    # Preprocess the DataFrame (remove spaces from column names)
    df.columns = df.columns.str.replace(' ', '')
    
    # Prepare the request payload
    payload = {
        "table": df.to_dict(orient="records"),
        "query": question
    }

    # Send a POST request to the TAPAS API endpoint
    api_endpoint = "https://api-inference.huggingface.co/models/google/tapas-large-finetuned-wtq"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Replace YOUR_API_KEY with your actual API key

    try:
        response = requests.post(api_endpoint, json=payload, headers=headers)
        response.raise_for_status()

        query_result = response.json()
        st.write("Query Result:")
        st.write(query_result['answer'])
    except requests.exceptions.RequestException as e:
        st.write(f"Error making API request: {e}")