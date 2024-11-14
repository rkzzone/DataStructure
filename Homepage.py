import streamlit as st

st.set_page_config(
    page_title="Projects Data Structures"
)

st.title("Main Page")

queue = st.Page(
    page="Projects/Homepage.py"
)

st.sidebar.success("Select a Page Above")
