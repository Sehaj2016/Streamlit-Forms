import streamlit as st

with st.form("registration_form"):
    st.subheader("Create an Account")
    new_user = st.text_input("Choose a Username")
    email = st.text_input("Email Address")
    new_pass = st.text_input("Password", type="password")
    confirm_pass = st.text_input("Confirm Password", type="password")
    register = st.form_submit_button("Register")

    if register:
        if new_pass == confirm_pass:
            st.info("Registration logic: Save data to database.")
        else:
            st.error("Passwords do not match.")