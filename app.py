import streamlit as st
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Function to analyze severity
def analyse_severity(user_message):
    prompt = f"""
    Analyse the severity of the following message and categorize it into 'Low', 'Medium', or 'High' severity. 
    Also, summarize the message by highlighting only the most important keywords. 
    Output in the following format:
    
    Severity: <Low/Medium/High>
    Summary: <Summarized Message>
    
    Message: {user_message}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()

# Set page config
st.set_page_config(page_title="HH Hackfest - Severity Analysis", page_icon="🧠", layout="wide")

# Sidebar Info
with st.sidebar:
    st.header("About this App 🧠")
    st.markdown("""
        This tool helps **therapists** prioritize incoming messages by:
        - Classifying **severity** (Low, Medium, High)
        - Providing a **concise summary**
        
        Built for **HH Hackfest**.
    """)

# Main Title
st.title("📬 Message Severity Analyzer")

# Input Box
st.markdown("### Type a message below to analyze its severity:")
user_message = st.text_area("Your message", height=100)

# Process Message
if st.button("Analyze"):
    if user_message.strip():
        with st.spinner("Analyzing..."):
            result = analyse_severity(user_message)

        # Extract severity and summary
        try:
            severity_line, summary_line = result.split('\n', 1)
            severity = severity_line.replace("Severity:", "").strip()
            summary = summary_line.replace("Summary:", "").strip()

            # Show results
            st.success("✅ Analysis Complete")

            severity_colors = {
                "Low": "🟢 Low",
                "Medium": "🟡 Medium",
                "High": "🔴 High"
            }

            st.markdown(f"**Severity:** {severity_colors.get(severity, severity)}")
            st.markdown(f"**Summary:** _{summary}_")

        except Exception:
            st.error("⚠️ Couldn't parse the response. Please try again.")

    else:
        st.warning("Please type a message before analyzing.")
