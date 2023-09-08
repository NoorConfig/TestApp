# simple_app.py

import streamlit as st

st.title("Simple Streamlit App")

st.write("If you see this text, your Streamlit app is working!")

# Let's also add a simple interactive widget
number = st.slider("Pick a number", 1, 100)
st.write(f"You picked {number}")
