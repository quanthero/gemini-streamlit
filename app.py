import streamlit as st
import os
import google.generativeai as genai

access_token = os.environ["APIKEY"]
# Configure the API key
genai.configure(api_key=access_token)

# Streamlit UI setup
st.set_page_config(page_title="🤗💬 Chat with AI")

# App title
st.title('🤗💬 Chat with AI')

# Store LLM generated responses
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating AI response
def generate_response(prompt_input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt_input)
    return response.text

# User-provided prompt
#if prompt := st.chat_input():
#    st.session_state.messages.append({"role": "user", "content": prompt})
#    with st.spinner("Thinking..."):
#        response = generate_response(prompt)
#    message = {"role": "assistant", "content": response}
#    st.session_state.messages.append(message)

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("Thinking..."):
        response = generate_response(prompt)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

    # Force rerun to update chat
    st.experimental_rerun()
