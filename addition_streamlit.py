import streamlit as st

# Set page title
st.title("Hello")

# Add a text input widget
user_input1 = st.text_input("Enter a number:")
user_input2 = st.text_input("Enter a number:")
answer = user_input1 + user_input2

# Display a greeting message
st.write(f" {user_input1}+ {user_input2} = {answer}")