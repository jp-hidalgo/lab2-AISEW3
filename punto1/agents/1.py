import os
from dotenv import load_dotenv, find_dotenv
from autogen import ConversableAgent

# Load environment variables
load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GOOGLE_API_KEY")
llm_config = {"model": "gemini-1.5-flash-latest", "api_key": gemini_api_key, "api_type": "google"}

# Define agents with neutral system messages
cathy = ConversableAgent(
    name="cathy",
    system_message="Your name is Cathy and you are a comedian who loves making people laugh.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

joe = ConversableAgent(
    name="joe",
    system_message="Your name is Joe and you are a comedian who enjoys witty banter. Start the next joke from the punchline of the previous joke.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# Initiate chat
try:
    chat_result = joe.initiate_chat(
        recipient=cathy,
        message="I'm Joe. Cathy, let's keep the jokes rolling.",
        max_turns=2,
    )

    # Continue the conversation
    cathy.send(message="What's the last joke we said?", recipient=joe, request_reply=True)

except RuntimeError as e:
    print(f"An error occurred during the conversation: {e}")
