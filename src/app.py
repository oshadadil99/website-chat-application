import streamlit as st

st.set_page_config(page_title="Chat with any website ",page_icon="🧛‍♂️" )
st.title("Chat with any website with prince Vlad 🧛‍♂️")

with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

user_query = st.chat_input("Ask anything from prince vlad...")
if user_query is not None and user_query != "":

    with st.chat_message("Human"):
        st.write(user_query)

    with st.chat_message("AI"):
        st.write("mn dnne ne ")

