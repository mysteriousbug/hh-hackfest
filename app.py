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

# Initialize session state for storing messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Message input area
user_message = st.text_input("Type your message:")

# Send button
if st.button("Send"):
    if user_message:
        # Simulate sentiment analysis (you can replace this with your AI model)
        severity, color = analyze_severity(user_message)
        
        # Add the new message to the history
        st.session_state.messages.append((user_message, severity, color))
    else:
        st.write("Please type a message before sending.")

# Display message history
for message, severity, color in st.session_state.messages:
    st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px;">'
                f'<strong>{severity}:</strong> {message}</div>', unsafe_allow_html=True)
