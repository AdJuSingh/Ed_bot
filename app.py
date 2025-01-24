import streamlit as st
import requests
from PIL import Image
import random
import time

# Streamlit Frontend for Rasa Chatbot
st.set_page_config(page_title="LearnAI", page_icon="🤖", layout="wide")

# Custom CSS for Vibrancy & Interactivity
st.markdown("""
<style>
/* Global Background */
body {
    background: linear-gradient(to right, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1, #fad0c4, #ff9a9e);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Poppins', sans-serif;
    color: #333;
}

/* Sidebar Styling */
.sidebar-title {
    font-size: 22px;
    font-weight: bold;
    color: #2d3436;
    margin-bottom: 15px;
    text-shadow: 1px 1px #dfe6e9;
}

.sidebar-section {
    background: linear-gradient(135deg, #74ebd5, #acb6e5);
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 15px;
    color: white;
    font-weight: bold;
    transition: transform 0.3s, background 0.3s;
}

.sidebar-section:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg, #a1c4fd, #c2e9fb);
}

/* Chat Container */
.chat-container {
    max-height: 600px;
    overflow-y: auto;
    padding: 15px;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

/* Chat Bubbles */
.chat-message {
    padding: 15px;
    border-radius: 15px;
    margin: 10px 0;
    max-width: 75%;
    word-wrap: break-word;
    font-size: 16px;
    font-weight: 500;
    animation: fadeIn 0.4s ease-in-out;
}

.chat-message.user {
    background: linear-gradient(to right, #4facfe, #00f2fe);
    color: white;
    text-align: left;
    margin-left: auto;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.3);
}

.chat-message.bot {
    background: linear-gradient(to right, #fad0c4, #fbc2eb);
    color: #333;
    text-align: left;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.3);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(to right, #ff9966, #ff5e62);
    color: white;
    border: none;
    border-radius: 20px;
    padding: 10px 20px;
    transition: transform 0.3s ease, background 0.3s ease-in-out;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

.stButton>button:hover {
    background: linear-gradient(to right, #ff5e62, #ff9966);
    transform: scale(1.1);
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
}

/* Floating Action Button */
.floating-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: white;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    text-align: center;
    font-size: 30px;
    line-height: 60px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    cursor: pointer;
    animation: bounce 2s infinite;
}

.floating-btn:hover {
    background: linear-gradient(to right, #2575fc, #6a11cb);
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>
""", unsafe_allow_html=True)

# Sidebar Branding
st.sidebar.image("Image.jpeg", caption="LearnAI", use_container_width=True)
st.sidebar.markdown('<h2 class="sidebar-title">AI/ML Chatbot</h2>', unsafe_allow_html=True)
st.sidebar.markdown("""
<div class="sidebar-section">
📚 Learn interactively about AI, ML, DevOps, and more!
</div>
<div class="sidebar-section">
🚀 Key Features:
<ul>
  <li>Dynamic Learning Suggestions</li>
  <li>Interactive Visuals</li>
  <li>AI Fun Facts</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Floating Help Button
st.markdown('<div class="floating-btn">❓</div>', unsafe_allow_html=True)

# Main Page Header
st.title("Welcome to LearnAI! 🤖")
st.markdown("""
Your vibrant, interactive chatbot for AI/ML learning!  
Type your queries below and enjoy the experience. 🌈
""")

# Backend URL (Update with your Rasa server endpoint)
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
def display_chat():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state["messages"]:
        if msg["sender"] == "user":
            st.markdown(f'<div class="chat-message user">YOU: {msg["text"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot">BOT: {msg["text"]}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# User input field
st.markdown("### Ask me anything about AI/ML:")
user_input = st.text_input("", "", placeholder="Type your message here...")

# Send user input to the bot
if st.button("Send") and user_input:
    st.session_state["messages"].append({"sender": "user", "text": user_input})
    try:
        response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_input})
        response_data = response.json()
        for bot_message in response_data:
            st.session_state["messages"].append({"sender": "bot", "text": bot_message["text"]})
    except Exception as e:
        st.error(f"Error communicating with the bot: {e}")

# Display updated chat
display_chat()

