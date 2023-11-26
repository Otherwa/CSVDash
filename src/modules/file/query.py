import streamlit as st
from dotenv import load_dotenv
import os
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
from pandasai.responses.response_parser import ResponseParser
import matplotlib

matplotlib.use(backend="TkAgg")

load_dotenv()


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


# Query CSV using LangChain and Hugging Face's Inference API
def query_csv_transformers(df, user_question, api):
    llm = OpenAI(api_token=openai_api_key)
    if api:
        pandas_ai = SmartDataframe(
            df,
            config={
                "llm": llm,
                "save_charts": True,
                "save_charts_path": r"./data/charts",
            },
        )
        response = pandas_ai.chat(user_question)
        print(response)
        if response == None:
            return {"answer": None}
        return {"answer": response}
