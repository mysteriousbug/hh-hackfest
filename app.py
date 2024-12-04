import streamlit as st

# Simple function to simulate sentiment analysis on the message
def analyze_severity(message):
    if "pain" in message.lower() or "can't" in message.lower():
        return "High Severity", "red"
    elif "okay" in message.lower() or "good" in message.lower():
        return "Low Severity", "green"
    else:
        return "Medium Severity", "yellow"

# Streamlit Layout
st.title('Physical Therapy Messaging App')

# Instructions
st.write("This is a simple app to simulate a messaging interface with sentiment analysis for physical therapy.")

# Message input area
user_message = st.text_input("Type your message:")

# Send button
if st.button("Send"):
    if user_message:
        # Simulate sentiment analysis (you can replace this with your AI model)
        severity, color = analyze_severity(user_message)
        
        # Display message with severity color
        st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px;">'
                    f'<strong>{severity}:</strong> {user_message}</div>', unsafe_allow_html=True)
    else:
        st.write("Please type a message before sending.")
