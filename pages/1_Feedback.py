import streamlit as st
import os
from datetime import datetime
import pandas as pd


FEEDBACK_COLUMN_ONE = "Date"
FEEDBACK_COLUMN_TWO = "Summary"
FEEDBACK_COLUMN_THREE = "Feedback"
FEEDBACK_CSV = "feedback.csv"

# needful functions
def disabled():
    st.session_state.disabled = True


def update_feedback(interact_date, user_summary, user_feedback):
    if not os.path.exists(FEEDBACK_CSV):
        feedback_data = pd.DataFrame(columns = [FEEDBACK_COLUMN_ONE, FEEDBACK_COLUMN_TWO, FEEDBACK_COLUMN_THREE])
        feedback_data.to_csv(FEEDBACK_CSV, index = False)

    feedback_df = pd.read_csv(FEEDBACK_CSV)

    metadata = {}
    metadata[FEEDBACK_COLUMN_ONE] = interact_date
    metadata[FEEDBACK_COLUMN_TWO] = user_summary
    metadata[FEEDBACK_COLUMN_THREE] = user_feedback
    feedback_df_new = pd.concat([feedback_df, pd.DataFrame(metadata, index = [0])], ignore_index = True)
    feedback_df_new.to_csv(FEEDBACK_CSV, index = False)
    print("Saved successfully")
    return True


if 'summary' not in st.session_state:
    st.session_state.summary = None

st.title("We value Your FeedBack")

if not st.session_state.summary:
    st.error("Please Upload a pdf and generate a summary before giving feedback", icon = "🚨")

else:
    st.subheader("Please provide your feedback with web interaction")
    st.markdown("**Are you satidfied with the service?**")
    # feedback state
    feedback_state = False

    #create columns
    col1, col2 = st.columns(2)

    with col1:
        #set feedback buttons
        if st.button("Yes", type = "primary", on_click=disabled, disabled=st.session_state.disabled, use_container_width = True):
            feedback_state = update_feedback(datetime.now(), st.session_state.summary, "Yes")

    with col2:
        if st.button("No", type = "primary", on_click=disabled, disabled=st.session_state.disabled, use_container_width = True):
            feedback_state = update_feedback(datetime.now(), st.session_state.summary, "No")

    #say thank you if the feedback is given
    if feedback_state:
        st.header("Thank You For Your Feedback!")