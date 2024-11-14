import streamlit as st

queue_page = st.Page(
    page="Projects/Queue.py",
    title="Queue",
    default=True,
)

homepage_page = st.Page(
    page="Projects/Homepage.py",
    title="Homepage",
)

projects_page = st.Page(
    page="Projects/Project.py",
    title="Project",
)

stack_page = st.Page(
    page="Projects/Stack.py",
    title="Stack",
)

pg = st.navigation(pages=[queue_page, homepage_page, projects_page, stack_page])

pg.run()