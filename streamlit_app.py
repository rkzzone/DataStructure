import streamlit as st

st.set_page_config(
    page_title="Projects Data Structures"
)

queue_page = st.Page(
    page="Projects/Queue.py",
    title="Queue",
    default=True,
)

pg = st.navigation(pages=[queue_page])

pg.run()