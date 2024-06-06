from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
import prompts
from event_details import EventDetails
import streamlit as st

_ = load_dotenv(find_dotenv())
# Set up your OpenAI API key
client = OpenAI(
    # this is also the default, it can be omitted
    api_key=st.secrets.openai.openai_api_key,
)

# Initialize session state for storing the summary
if 'summary' not in st.session_state:
    st.session_state.summary = "Your summary will appear here after submission."


def get_summary():
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Update session state with the result
    st.session_state.summary = completion.choices[0].message.content


# User Interface
st.title('Proposal AI')

col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)
with col1:
    model = st.radio("Select Model", ["gpt-3.5-turbo", "gpt-4"])
with col2:
    temperature = float(st.select_slider("Temperature", options=[
        0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]))
with col3:
    max_tokens = int(st.number_input(
        "Max tokens", step=50, min_value=100, max_value=1000))
with col4:
    event_name = st.text_input("Event name")
    description = st.text_area("Description")
    club = st.text_input("Club")

with col5:
    date = st.date_input("Date")
    start_time = st.time_input("Start Time")
    end_time = st.time_input("End Time")
    venue = st.text_input("Venue")

event = EventDetails(
    title=event_name,
    description=description,
    club=club,
    date=date,
    start_time=start_time,
    end_time=end_time,
    venue=venue
)
messages = [
    {"role": "system", "content": prompts.system_message},
    {"role": "user", "content": prompts.get_prompt(event)}
]

st.button("Submit", on_click=get_summary)
# Display the summary
st.write(st.session_state.summary)
