import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os


FEEDBACK_COLUMN_THREE = "Feedback"
FEEDBACK_CSV = "feedback.csv"


st.title("Dashboard")

st.header("Feedback Analysis")
st.subheader("Feedback Data")

if not os.path.exists(FEEDBACK_CSV):
    st.error("Take Some Feedbacks from Users to view the Analytics 🚨")
else:
    #read the data
    feedbacks = pd.read_csv(FEEDBACK_CSV)
    st.dataframe(feedbacks)
    #count plot
    sns.set_theme(style="whitegrid", palette="pastel")
    chart_fig = plt.figure(figsize=(5,5))
    sns.countplot(data = feedbacks, x = FEEDBACK_COLUMN_THREE)
    plt.xlabel("Feedback")
    plt.ylabel("Count")
    plt.title("Feedback Distribution")
    st.pyplot(chart_fig)