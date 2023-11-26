from datetime import datetime
import streamlit as st


# Custom Dependencies
import pandas as pd
from src.modules.file.chart_gen import generate_charts
from src.modules.file.edit_data import edit_data
from src.modules.file.mongodb import push_to_mongodb
from src.modules.file.query import query_csv_transformers


# Initialize a variable to store the DataFrame
df = None
history = []
counter = 0


def page_file(uploaded_file):
    # Global dataframe
    global df, history, counter

    if uploaded_file is not None:
        if df is None:
            # Read the uploaded CSV file into a DataFrame
            df = pd.read_csv(uploaded_file, index_col=False)

        df.dropna(how="all", inplace=True)
        # ? Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        st.write(f"DataFrame Created at: {current_time}")

        # ? Genrate Charts
        generate_charts(df)

        # ? Editable Dataframe
        df = edit_data(df)

        # ? Querier
        question = st.text_area("Your Query")

        # ? query
        if question:
            ans = query_csv_transformers(df, question, True)
            print(ans)
            # ? Store the question and answer in the history
            history.append(
                {
                    "question": question,
                    "answer": ans["answer"]
                    if ans["answer"] is not None
                    else "Plot Shown",
                }
            )
            # ? Display the answer in Streamlit
            st.success(ans["answer"] if not None else "Plot Shown")
            counter += 1

            # Button to push records to MongoDB
            if st.button("Push to MongoDB", disabled=True):
                if df is not None:
                    # Call the push_to_mongodb function
                    push_to_mongodb(df, "files", uploaded_file.name.split(".")[0])
                    st.success("Records pushed to MongoDB successfully")
                else:
                    st.warning("DataFrame is empty. Upload a file first")

            # ? Display history in Streamlit
            if history:
                st.subheader("Question-Answer History:")
                for i, entry in enumerate(history[::-1], 1):
                    with st.status(f"Question {i}", expanded=False) as status:
                        status.write(f"Question: {entry['question']}")
                        status.write(f"Answer: {entry['answer']}")

    else:
        st.error("File not uploaded or present")
        history.clear()
