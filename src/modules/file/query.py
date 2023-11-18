import streamlit as st
from dotenv import load_dotenv
import os
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Instantiate LLM once
llm = OpenAI(api_token=openai_api_key)


@st.cache_resource()
def SmartDataSet(df):
    return SmartDataframe(df, config={"llm": llm})


# Query CSV using LangChain and Hugging Face's Inference API
def query_csv_transformers(df, user_question):
    pandas_ai = SmartDataSet(df)
    with st.spinner("Querying Data 🔍"):
        st.write("Please Wait ⏳")
        response = pandas_ai.chat(user_question)
        st.success(response)
