# custom dependecies
from css.css import myStyle

# dependencies
import streamlit as st
import pandas as pd


def main():
    # config
    st.markdown(myStyle, unsafe_allow_html=True)
    st.set_option("deprecation.showfileUploaderEncoding", False)

    # Add a sidebar for navigation
    st.sidebar.title("CSVDash")
    page = st.sidebar.selectbox("Pages:", ["Home", "Upload CSV"])

    if page == "Home":
        # Home page content
        st.title("Welcome to CSV File Viewer")
        st.write(
            "This app allows you to upload a CSV file and view its contents in a table."
        )
        # Display a GIF from a URL
        st.image(
            "https://i.pinimg.com/originals/e6/10/9e/e6109e32a9ac1a8f2496d7fba78e9c84.gif"
        )

    elif page == "Upload CSV":
        # File upload page
        st.title("Upload a CSV File")
        st.write("Upload a CSV file below:")
        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

        if uploaded_file is not None:
            # Read the uploaded CSV file into a DataFrame
            df = pd.read_csv(uploaded_file)

            # Display the DataFrame as a table
            st.write("Table View:")
            st.write(df)

            # Allow users to select columns for analysis
            selected_columns = st.multiselect(
                "Select columns for analysis:", df.columns
            )

            if selected_columns:
                # Display selected columns
                st.write("Selected Columns:")
                st.write(df[selected_columns])

                # Statistical analysis
                if st.button("Calculate Statistics"):
                    st.write("Statistics:")
                    try:
                        for column in selected_columns:
                            st.subheader(f"Column: {column}")
                            st.write(f"Mean: {df[column].mean()}")
                            st.write(f"Mode: {df[column].mode()[0]}")
                            st.write(f"Standard Deviation: {df[column].std()}")
                            st.write(f"Variance: {df[column].var()}")

                    except Exception as e:
                        print(e)
                        st.error(f"One of the Columns is not Quantitative")


if __name__ == "__main__":
    st.set_page_config(
        page_title="CSVDash",  # Set your desired title here
        page_icon=":chart_with_upwards_trend:",  # Set your desired favicon (emoji) here
    )
    st.set_option("deprecation.showfileUploaderEncoding", False)
    main()
