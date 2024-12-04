import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-KwWxwH8OrEWA9Yd-sDC7LwyVHasUgCObWBNcPn6LdTnoP2psNCdT1JoGapUQGjKqIieaEDqCsT3BlbkFJLg0vyeferOctq__9f0bKMMuDU6q2XtSO88LsN33q-ySln3EXIthWbDXau06qsZc9CuzNZRTsgA'

# Function to use GPT-4 for analyzing message severity
def analyze_severity_with_gpt(message):
    # Construct a prompt for GPT-4 to assess message severity
    prompt = f"""
    You are a virtual assistant trained to analyze messages from physical therapy patients. Based on the message content, classify its severity into one of the following categories:
    - Low Severity
    - Medium Severity
    - High Severity
    
    The message is: "{message}"

    Please return only the severity category (Low, Medium, High).
    """
    
    # Call OpenAI's GPT-4 API
    response = openai.Completion.create(
        model="gpt-4",  # or use "gpt-3.5-turbo" for faster processing
        prompt=prompt,
        max_tokens=10,  # Limit the response to just the severity classification
        temperature=0.2,  # Keep it deterministic (low temperature)
    )
    
    # Extract the severity classification from the response
    severity = response.choices[0].text.strip()
    return severity

# Streamlit Layout
st.title('Physical Therapy Messaging App')

# Instructions
st.write("This app allows physical therapy patients to send messages and get real-time severity classification based on the content of their messages.")

# Message input area
user_message = st.text_input("Type your message:")

# Send button
if st.button("Send"):
    if user_message:
        # Analyze message severity using GPT-4
        severity = analyze_severity_with_gpt(user_message)
        
        # Display message with severity color
        if severity == "High Severity":
            color = "red"
        elif severity == "Medium Severity":
            color = "yellow"
        else:
            color = "green"
        
        st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px;">'
                    f'<strong>{severity}:</strong> {user_message}</div>', unsafe_allow_html=True)
    else:
        st.write("Please type a message before sending.")

