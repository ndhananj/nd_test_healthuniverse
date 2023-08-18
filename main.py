import streamlit as st

st.title("Welcome to our ECG Tech in a Box!")
st.write("Right now the application just lets you upload as zip file.")

image_file = st.file_uploader('Upload zip file with the ECG data', type=['zip'])