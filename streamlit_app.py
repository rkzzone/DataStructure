import streamlit as st

st.set_page_config(
    page_title="Projects Data Structures"
)

queue_page = st.Page(
    page="Projects/Queue.py",
    title="Queue",
    default=True,
)

homepage_page = st.Page(
    page="Projects/Homepage.py",
    title="Homepage",
    default=True,
)

projects_page = st.Page(
    page="Projects/Project.py",
    title="Project",
    default=True,
)

pg = st.navigation(pages=[queue_page])

pg.run()