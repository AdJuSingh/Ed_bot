import streamlit as st
import requests
from PIL import Image

# Streamlit Frontend for Rasa Chatbot
st.set_page_config(page_title="AI/ML Educational Chatbot", page_icon="🤖", layout="wide")

# Sidebar Branding
st.sidebar.image("Image.jpeg", caption="Chatbot Logo", use_container_width=True)
st.sidebar.title("AI/ML Educational Chatbot")
st.sidebar.markdown("Learn about AI, ML, DevOps, and more in an interactive way! 📚")

# Main Page Header
st.title("AI/ML Educational Chatbot")
st.markdown("""
<style>
.chat-message {
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
    max-width: 70%;
    word-wrap: break-word;
}
.chat-message.user {
    background-color: #dff9fb;
    text-align: left;
    margin-left: auto;
}
.chat-message.bot {
    background-color: #c7ecee;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# Backend URL (Update this with your Rasa server endpoint)
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
def display_chat():
    for msg in st.session_state["messages"]:
        if msg["sender"] == "user":
            st.markdown(f'<div class="chat-message user">YOU: {msg["text"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot">BOT: {msg["text"]}</div>', unsafe_allow_html=True)

# User input field with enhanced styling
st.markdown("**Ask me anything about AI/ML:**")
user_input = st.text_input("", "", placeholder="Type your message here...")

# Send user input to the bot
if st.button("Send") and user_input:
    # Append user message to chat history
    st.session_state["messages"].append({"sender": "user", "text": user_input})

    # Send request to Rasa bot
    try:
        response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_input})
        response_data = response.json()

        # Process and append bot responses
        for bot_message in response_data:
            st.session_state["messages"].append({"sender": "bot", "text": bot_message["text"]})
    except Exception as e:
        st.error(f"Error communicating with the bot: {e}")

# Display updated chat history
display_chat()

# Additional Features Section
st.sidebar.title("Additional Features")
st.sidebar.markdown(
    """
    - 🔗 **Fetch YouTube Videos** based on discussed topics.
    - 🔍 **Generate AI/ML Content** dynamically.
    - 🔄 **Save Chat History** for future reference.
    """
)

# Tests Placeholder
st.sidebar.title("Bot Test Cases")
st.sidebar.markdown("""
Use these to evaluate bot behavior:
- 😊 Greet and respond happily
- 😔 Handle unhappy moods
- 🕵️ Answer bot challenge
- 🙋🏻 Say goodbye
- 🔧 Respond to creator query
""")

# Footer Section
st.sidebar.markdown("""
---
Created with ❤️ by Aditi
""")
