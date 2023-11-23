import streamlit as st
from dotenv import load_dotenv
import os
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
from pandasai.callbacks import BaseCallback
from pandasai.responses.response_parser import ResponseParser
import matplotlib.pyplot as plt

load_dotenv()

class StreamlitCallback(BaseCallback):
    def __init__(self, container) -> None:
        """Initialize callback handler."""
        self.container = container

    def on_code(self, response: str):
        self.container.code(response)


class StreamlitResponse(ResponseParser):
    def __init__(self, context) -> None:
        super().__init__(context)

    def format_dataframe(self, result):
        st.dataframe(result["value"])
        return

    def format_plot(self, result):
        st.image(result["value"])
        return

    def format_other(self, result):
        st.write(result["value"])
        return

openai_api_key = os.getenv("OPENAI_API_KEY")

# Instantiate LLM once
llm = OpenAI(api_token=openai_api_key)

def SmartDataSet(df):
    return SmartDataframe(df, config={"llm": llm})


# Query CSV using LangChain and Hugging Face's Inference API
def query_csv_transformers(df, user_question):
    pandas_ai = SmartDataSet(df)
    with st.spinner("Querying Data 🔍"):
        st.write("Please Wait ⏳ Generaly Takes a Little Time")
        response = pandas_ai.chat(user_question)
        print(response)
        with st.status("Analyzing Data 🔍", expanded=False) as status:
            status.update(label="Computing...")
            st.write(response) if response != None else st.write("") 
            st.image('./temp_chart.png')
            status.update(label="Computed ✅")
