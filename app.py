import streamlit as st
from chatbot import get_response


st.set_page_config(
    page_title="EventEase Chatbot",
    page_icon="📅",
    layout="centered"
)


st.title("📅 EventEase Chatbot")
st.write("Your simple assistant for events and announcements.")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_input = st.chat_input("Ask me about an event...")


if user_input:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = get_response(user_input)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()