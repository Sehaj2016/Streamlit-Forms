import streamlit as st
import pandas as pd

st.title("Hello Streamlit!")
st.text("Welcome to my Streamlit app.")
st.write("This is a simple Streamlit app.")
st.markdown('bold text')
st.header("Header")
st.subheader("Subheader")
# Text input
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")
number = st.number_input("Enter a number:")
st.write(f"You entered: {number}")
if st.button("Click Me"):
    st.write("Button clicked!")
option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

file = st.file_uploader("Upload a file:")

csv_path = r"C:\Users\Jasminder\Downloads\archive(3)\covid_data.csv"
df = None

try:
    source = file if file else csv_path
    df = pd.read_csv(source, sep=None, engine='python', on_bad_lines='warn')
    st.success("Data loaded successfully.")
except Exception as e:
    st.error(f"Could not read CSV data: {e}")

if df is not None:
    st.dataframe(df)
    st.line_chart(df)
    st.bar_chart(df)

# sidebar
st.sidebar.title("Sidebar")
options = st.sidebar.multiselect("Select options:", ["Option A", "Option B", "Option C"])

    