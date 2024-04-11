import streamlit as st

# Set page title
st.title("Hello")

# Add a text input widget
user_input1 = st.text_input("Enter a number:")




# Display a greeting message
st.write(f" {user_input1}")