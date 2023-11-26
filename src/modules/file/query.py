import streamlit as st
from dotenv import load_dotenv
import os
from pandasai import SmartDataframe, BaseCallback
from pandasai.llm.openai import OpenAI
from pandasai.responses.response_parser import ResponseParser
from transformers import pipeline
import matplotlib

matplotlib.use(backend="TkAgg")

load_dotenv()


openai_api_key = os.getenv("OPENAI_API_KEY")


# Query CSV using LangChain and Hugging Face's Inference API
def query_csv_transformers(df, user_question, api):
    llm = OpenAI(api_token=openai_api_key)
    if api:
        pandas_ai = SmartDataframe(df, config={"llm": llm})
        response = pandas_ai.chat(user_question)
        print(response)
        return {"answer": response}
