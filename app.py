import streamlit as st
import requests

st.title("AI/ML Educational Chatbot")
st.write("Ask me anything about Artificial Intelligence or Machine Learning!")

user_input = st.text_input("Your Question:")
if st.button("Ask"):
    if user_input:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": user_input},
        )
        for res in response.json():
            st.write(res.get("text", ""))
