import streamlit as st
st.title("Feedback Form")
name = st.text_input("Name")
email = st.text_input("Email")
feedback = st.text_area("Your Feedback")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")  
    