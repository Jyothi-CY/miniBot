import streamlit as st
from services.gemini_service import get_gemini_response
from components.chat_ui import render_chat_bubble, inject_css

st.set_page_config(page_title="Mini Bot", layout="centered")

inject_css()

st.title("🌟 Mini Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    render_chat_bubble("ai", "🌸 Hi there! I'm Mini Bot — your AI bestie! Ask me anything: coding help, project ideas, or even what's for lunch — I'm here for it ✨")

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    
    for role, msg in st.session_state.messages:
        render_chat_bubble(role, msg)
    
    with st.spinner("Mini Bot is typing..."):
        full_history = st.session_state.messages.copy()
        reply = get_gemini_response(full_history)
        st.session_state.messages.append(("model", reply))
    st.rerun()
    
else:
    for role, msg in st.session_state.messages:
        render_chat_bubble(role, msg)
