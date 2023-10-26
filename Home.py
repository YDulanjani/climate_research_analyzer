import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from datetime import datetime
import tiktoken
from utils import pdf_to_text, generate_summary, save_vector_store, retrieval_augmented_generation


IMAGE = "https://miro.medium.com/v2/resize:fit:1400/1*02uoHJoYt3E7rylWEny02w.jpeg"
PROMPT = """
Write a summary of the following which anybody can understand and learn what is saying in the research. Summary should be in simple terms and emphasise the contribution towards environmental Science :
{text}
CONCISE SUMMARY:
"""

#disable in session state
if 'disabled' not in st.session_state:
    st.session_state.disabled = False

if 'store' not in st.session_state:
    st.session_state.store = None

if 'summary' not in st.session_state:
    st.session_state.summary = None
print(st.session_state)


# variables
summary = None
saved_vector_store = None

# web design

# title
st.title('Climate Change Research Analyzer')

# image
st.image(IMAGE, caption="Climate Changes")

#tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Question Answering", "Feedbacks", "Dashboard"])

# upload a research
st.subheader("Please Upload a Research Article in PDF Format")
pdf = st.file_uploader("Upload PDF file",type="pdf")

if pdf:
    with st.spinner("Extracting Texts and Getting the Summary..."):
        extracted_text = pdf_to_text(pdf)
        if extracted_text:
            st.toast("Text Extraction Completed!!! 👍")

        summary = generate_summary(extracted_text, PROMPT)
        if summary:
             st.session_state.summary = summary
             st.toast("Summary Generation is completed! 👍")

        saved_vector_store = save_vector_store(extracted_text)
        if saved_vector_store:
            st.session_state.store = saved_vector_store
            st.toast("Saved to the Vector Store! 👍")

        with st.expander("View Extracted Text"):
                st.subheader("Extracted Text from the PDF")
                st.write(extracted_text)

        # summary
        st.subheader("Generated Summary")
        st.write(summary)

                    



