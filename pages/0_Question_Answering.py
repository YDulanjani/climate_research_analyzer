import streamlit as st
from utils import retrieval_augmented_generation


if 'store' not in st.session_state:
    st.session_state.store = None

st.title("Question Answering Feature")

if not st.session_state.store:
    st.error("Please Upload a pdf in Home page and try again", icon = "🚨")

else:
    question = st.text_input("Enter Your Question...")
    if question:
        with st.status("Fetching the Answer"):
            response = retrieval_augmented_generation(question, st.session_state.store)
            st.write(response)