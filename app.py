import os
from lyzr_agent_api import AgentAPI, ChatRequest
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
LYZR_API_KEY = os.getenv("LYZR_API_KEY")
AGENT_ID = os.getenv("AGENT_ID")

# Streamlit page configuration
st.set_page_config(
    page_title="Financial Advisor Agent",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

# Display logo and title
image = Image.open("lyzr-logo.png")
st.image(image, width=150)
st.title("Financial Advisor Agent")
st.markdown("### Welcome to the Financial Advisor Agent!")

# Initialize the LyzrAgentAPI
client = AgentAPI(x_api_key=LYZR_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the past conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input area for new messages
user_message = st.chat_input("Type your message here...")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        response = client.chat_with_agent(
            json_body=ChatRequest(
                user_id="harshit@lyzr.ai",
                agent_id=AGENT_ID,
                message=user_message,
                session_id="sdfw",
            )
        )
        chat_response = response['response']
        response = st.write(chat_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": chat_response}
    )
    # Store user message in chat history


# Optional footer or credits
st.markdown("---")
st.markdown("Powered by Lyzr Agent API and OpenAI")
