import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def analyse_severity(user_message):
    prompt = f"Analyse the severity of the message {user_message} and categorize it into low, medium or gigh severity. Also, summarize the message highlighting only the mose important keywords. Output the severity and the summarized message."
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    summarized_message = response.choices[0].message.content.strip()
    return summarized_message

# Streamlit Layout
st.title('HH HACKFEST - MESSAGE SEVERITY ANALYSIS TOOL')

# Instructions
st.write("This is a simple app to simulate a messaging interface with sentiment analysis for physical therapy.")


# Message input area
user_message = st.text_input("Type your message:")

# Send button
if st.button("Send"):
    if user_message:
        # Simulate sentiment analysis (you can replace this with your AI model)
        severity = analyse_severity(user_message)
        
        # Add the new message to the history
        st.code(severity)
    else:
        st.write("Please type a message before sending.")



