# Custom dependencies
from css.css import myStyle

# Dependencies
import streamlit as st
import pandas as pd
import base64


def main():
    # Config
    st.markdown(myStyle, unsafe_allow_html=True)
    st.set_option("deprecation.showfileUploaderEncoding", False)

    st.sidebar.image(
        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8a97820c-3d54-44c5-bd33-224656c74360/d5a97ie-995eb26b-0e02-4b89-852d-fa1da79edd6b.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhhOTc4MjBjLTNkNTQtNDRjNS1iZDMzLTIyNDY1NmM3NDM2MFwvZDVhOTdpZS05OTVlYjI2Yi0wZTAyLTRiODktODUyZC1mYTFkYTc5ZWRkNmIuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.dReXRU3hJWw4Yr9Uk0RUqt0YnYuveewnjbCQiT9VbNE"
    )

    # Define the Streamlit app title and a brief description
    st.title("CSVdash - Convert & Visualize CSV Data")
    st.write("Welcome to CSVdash, your tool for converting and visualizing CSV data!")

    # Create a sidebar for file upload and data conversion options
    st.sidebar.header("Upload CSV File")
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    st.sidebar.write("Upload your CSV file on the left sidebar to get started.")

    # Add a sidebar for navigation
    st.sidebar.title("CSVDash")
    page = st.sidebar.selectbox(
        "Pages:",
        ["Home", "File", "Convert Column", "Plot Graph", "Download Data"],
    )

    # sidebar

    if page == "Home":
        # Home page content
        pass

    elif page == "File":
        if uploaded_file is not None:
            # Read the uploaded CSV file into a DataFrame
            df = pd.read_csv(uploaded_file, index_col=False)
            df.reset_index(drop=True, inplace=True)

            # Display the DataFrame as a table
            st.write("Table View:")
            st.write(df)
        else:
            st.error("File not Upload or Present")

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

    elif page == "Download Data":
        # Download data page
        st.title("Download Data")
        st.write("Select data to download:")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)

            if st.button("Download Data"):
                # Save the data to a file
                data_csv = df.to_csv(index=False)
                b64 = base64.b64encode(data_csv.encode()).decode()
                href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV</a>'
                st.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title="CSVDash",
        page_icon=":chart_with_upwards_trend:",
    )
    st.set_option("deprecation.showfileUploaderEncoding", False)
    main()
