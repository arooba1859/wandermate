import streamlit as st
from config import SYSTEM_PROMPT
from utils import get_chatbot_response

st.set_page_config(page_title="Wander Mate", page_icon="🧳")
st.title("🧳 Wander Mate - Your Travel Assistant")

# Tighten space below the title
st.markdown("<style>h1 { margin-bottom: 10px !important; }</style>", unsafe_allow_html=True)

# Load custom CSS safely
with open("styles.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Hello, I am Wander Mate. Ask me anything about your trip!"}
    ]

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        css_class = "user-message" if msg["role"] == "user" else "assistant-message"
        st.markdown(
            f'<div class="{css_class}"><pre style="white-space: pre-wrap; word-wrap: break-word;">{msg["content"]}</pre></div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)  # Close chat-container

# Chat input
user_input = st.chat_input("Ask about destinations, hotels, weather...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="user-message"><pre style="white-space: pre-wrap; word-wrap: break-word;">{user_input}</pre></div>',
        unsafe_allow_html=True
    )

    with st.spinner("Wander Mate is typing..."):
        try:
            reply = get_chatbot_response(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.markdown(
                f'<div class="assistant-message"><pre style="white-space: pre-wrap; word-wrap: break-word;">{reply}</pre></div>',
                unsafe_allow_html=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error("Something went wrong.")
            st.exception(e)
