"""
? chart_gen.py
++ file.py
"""

import streamlit as st
import time
import plotly.express as px


def generate_charts(dataframe):
    with st.status("Analyzing Data 🔍", expanded=False) as status:
        status.update(label="Computing...")
        time.sleep(1)

        # Display the column headers
        st.write("Column Headers:", ", ".join(dataframe.columns).title())
        # Calculate statistical data for quantitative columns
        quantitative_columns = dataframe.select_dtypes(include=[float, int])
        status.update(label="Generating Data Frame..")
        if not quantitative_columns.empty:
            # Convert None values to 0
            time.sleep(2)
            quantitative_columns = quantitative_columns.fillna(0)
            st.write("Statistical Data for Quantitative Columns:")
            # Define the column configuration
            column_config = {"textAlign": "center"}
            # Display the DataFrame with the specified column configuration
            st.dataframe(
                quantitative_columns.describe(), width=600
            )  # Adjust the width as needed
            # Create multiple interactive charts for each quantitative column
            st.write("Generating Charts...")
            time.sleep(1)
            st.write("Interactive Charts for Quantitative Columns:")
            for num, column in enumerate(quantitative_columns.columns, start=1):
                time.sleep(1)
                st.header(f"{num}. Charts for {column}")
                # Create an interactive histogram using Plotly
                fig_hist = px.histogram(
                    quantitative_columns,
                    x=column,
                    title=f"Histogram for {column}",
                )
                st.plotly_chart(fig_hist, use_container_width=True)
                # Create an interactive box plot using Plotly
                fig_box = px.box(
                    quantitative_columns,
                    x=column,
                    title=f"Box Plot for {column}",
                )
                st.plotly_chart(fig_box, use_container_width=True)
                # 2x2
                fig_hist = px.histogram(
                    quantitative_columns,
                    x=column,
                    title=f"Histogram for {column}",
                    width=500,
                )
                st.plotly_chart(fig_hist, use_container_width=True)
                # Create an interactive box plot using Plotly
                fig_box = px.box(
                    quantitative_columns,
                    x=column,
                    title=f"Box Plot for {column}",
                    width=500,
                )
                st.plotly_chart(fig_box, use_container_width=True)
                # Create an interactive scatter plot using Plotly
                fig_scatter = px.scatter(
                    quantitative_columns,
                    x=quantitative_columns.index,
                    y=column,
                    title=f"Scatter Plot for {column}",
                    width=500,
                )
                st.plotly_chart(fig_scatter, use_container_width=True)
                # Create an interactive violin plot using Plotly
                fig_violin = px.violin(
                    quantitative_columns,
                    x=column,
                    title=f"Violin Plot for {column}",
                    width=500,
                )
                st.plotly_chart(fig_violin, use_container_width=True)
            status.update(label="Computed ✅", state="complete", expanded=False)
        else:
            st.warning("No Quantitative Data Present in any Column 💀")
