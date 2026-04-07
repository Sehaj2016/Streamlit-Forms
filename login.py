import streamlit as st

with st.form("login_form"):
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

    if submit:
        # Add authentication logic here (e.g., check against a DB)
        st.success(f"Welcome, {username}!")