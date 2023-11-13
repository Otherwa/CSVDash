# Custom dependencies
from config.css import load_custom_css
from src.components.sidebar import create_sidebar

# pages
from src.file import page_file
from src.home import page_home

# Dependencies
import streamlit as st
import pandas as pd
import base64


def main():
    # Config
    load_custom_css()
    st.set_option("deprecation.showfileUploaderEncoding", False)

    # Create sidebar and get page and uploaded file
    page, uploaded_file = create_sidebar()

    if page == "Home":
        page_home()
    elif page == "File":
        page_file(uploaded_file)

    elif page == "Convert Column":
        # Convert column to quantitative data page
        st.title("Convert Column to Quantitative Data")
        st.write("Select a column and specify replacement options:")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            selected_column = st.selectbox("Select a column:", df.columns)
            if selected_column:
                st.write("Unique Non-Quanitative Data:")
                st.write([*df[selected_column].unique()])
                # Ask the user for replacement options as a list of tuples (old_value, new_value)
                st.write(
                    "Specify replacement options as 'old_value', 'new_value' for new value to ';'"
                )
                replacement_options = st.text_input(
                    "Enter replacement options (comma-separated):"
                )
                replacement_options = [
                    tuple(map(str.strip, r.split(",")))
                    for r in replacement_options.split(";")
                ]
                st.write(replacement_options)

            if st.button("Convert Column"):
                try:
                    # Apply user-defined replacements
                    for old_value, new_value in replacement_options:
                        df[selected_column] = df[selected_column].replace(
                            old_value, new_value
                        )

                    st.write("Updated DataFrame:")
                    st.write(df)

                    # Save the converted data to a file
                    if st.button("Download Converted Data"):
                        converted_data_csv = df.to_csv(index=False)
                        b64 = base64.b64encode(converted_data_csv.encode()).decode()
                        href = f'<a href="data:file/csv;base64,{b64}" download="converted_data.csv">Download CSV</a>'
                        st.markdown(href, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Conversion failed: {str(e)}")
        else:
            st.error("File not Upload or Present")
    elif page == "Plot Graph":
        # Plot graph page
        st.title("Plot Graph")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            selected_columns = st.multiselect("Select columns to plot:", df.columns)

            if selected_columns:
                chart_type = st.selectbox(
                    "Select chart type:", ["Line Chart", "Bar Chart"]
                )

                num_rows = st.slider(
                    "Number of Rows to Show in the Graph",
                    min_value=1,
                    max_value=df.shape[0],
                    value=min(10, df.shape[0]),
                )

                y_index = st.selectbox("Select Y-Index", selected_columns)
                if st.button("Plot Graph"):
                    data_to_plot = df[selected_columns].head(num_rows)
                    chart = None
                    if chart_type == "Line Chart":
                        df = pd.DataFrame(data_to_plot)
                        chart = st.line_chart(df.set_index([y_index]))
                    elif chart_type == "Bar Chart":
                        df = pd.DataFrame(data_to_plot)
                        chart = st.bar_chart(df.set_index([y_index]))
                    else:
                        st.warning("Select exactly two columns for Scatter Plot.")

                    if chart is not None:
                        pass
                    else:
                        st.warning(
                            "No chart selected or data columns not compatible with the selected chart type"
                        )
        else:
            st.error("File not Upload or Present")


if __name__ == "__main__":
    st.set_option("deprecation.showfileUploaderEncoding", False)
    # st.set_page_config(
    #     page_title="CSVDash",
    #     page_icon=":chart_with_upwards_trend:",
    # )

    main()
