import streamlit as st
import pandas as pd

VALID_USERS = {
    "user1": "password1",
    "user2": "password2"
}

def login_page():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in VALID_USERS and VALID_USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "main"
        else:
            st.error("Invalid username or password")

def data_page():
    st.title("Data")
    st.header("Upload Data")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"], key="file_uploader")

    if uploaded_file is not None:
        try:
            st.session_state.df = pd.read_csv(uploaded_file)
            st.session_state.file_uploaded = True

        except pd.errors.EmptyDataError:
            st.error("The uploaded file is empty. Please upload a valid CSV file.")
        except pd.errors.ParserError:
            st.error("Error parsing CSV file. Please upload a valid CSV file.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

    if 'df' in st.session_state and st.session_state.file_uploaded:
        df = st.session_state.df

        st.write("Data Preview:")
        st.write(df.head(10))

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Null Values")
            st.write(df.isnull().sum())

        with col2:
            st.subheader("Duplicated Values")
            st.write("Duplicated Values : ", df.duplicated().sum())

def data_visualization_page():
    st.title("Data visualization")
    st.write("This is where data visualization functionalities will be implemented.")

    if 'df' in st.session_state:
        df = st.session_state.df
    
        st.write("Data Preview:")
        st.write(df.head(10))

def data_cleansing_page():
    st.title("Data Cleansing")

    if 'df' in st.session_state:
        df = st.session_state.df

        st.write("Data Preview:")
        st.write(df.head(10))

        if st.button("Remove Duplicates"):
            df_cleaned = df.drop_duplicates()
            st.session_state.df = df_cleaned
            st.write("Duplicates removed.")
            st.write(df_cleaned.head())
    else:
        st.warning("No data available. Please upload data on the Data page.")

def data_preprocessing_page():
    st.title("Data Preprocessing")
    st.write("This is where data preprocessing functionalities will be implemented.")

def modeling_page():
    st.title("Modeling")
    st.write("This is where modeling functionalities will be implemented.")

def main_page():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Data", "Data Visualization", "Data Cleansing", "Data Preprocessing", "Modeling"], key="navbar")

    if selection == "Data":
        data_page()
    elif selection == "Data Visualization":
        data_visualization_page()
    elif selection == "Data Cleansing":
        data_cleansing_page()
    elif selection == "Data Preprocessing":
        data_preprocessing_page()
    elif selection == "Modeling":
        modeling_page()

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'page' not in st.session_state:
    st.session_state.page = "login"

if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False

if st.session_state.page == "main":
    main_page()
else:
    login_page()
