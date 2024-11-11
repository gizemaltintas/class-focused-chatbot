from openai import OpenAI
import streamlit as st
import re


openai_api_key = "OPEN_API_KEY"

st.title("💬 Class-Focused Chatbot")
st.caption("🚀 A Streamlit chatbot dedicated to your course content")

# Load and store class content from a text file
def load_class_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

class_content = load_class_content("class_info.txt")

# Function to extract significant keywords from the class content
def extract_keywords(content):
    # Extract words longer than 3 characters to filter out common words
    keywords = re.findall(r'\b\w{4,}\b', content.lower())
    return set(keywords)

class_keywords = extract_keywords(class_content)

# Initialize messages if not in session state
if "messages" not in st.session_state:
    # Adding the class content as a system message for initial context
    st.session_state["messages"] = [
        {"role": "system", "content": f"This is a course on Artificial Intelligence and Machine Learning. Here is the course information:\n\n{class_content}"},
        {"role": "assistant", "content": "How can I assist you with the class content?"}
    ]

# Display chat messages from session state
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Function to send message to OpenAI and get a response
def get_openai_response(prompt, messages):
    client = OpenAI(api_key=openai_api_key)
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        return response.choices[0].message.content
    except error.OpenAIError as e:
        st.error(f"OpenAI API error: {e}")
        return "I'm sorry, I encountered an error processing your request."

# Function to check if prompt is relevant to class content
def is_relevant_to_class(prompt):
    # Extract keywords from the user's prompt
    prompt_keywords = set(re.findall(r'\b\w{4,}\b', prompt.lower()))
    # Check for intersection with class keywords
    return bool(prompt_keywords & class_keywords)

# Capture user input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # Check for relevance
    if is_relevant_to_class(prompt):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # Get response from OpenAI
        msg = get_openai_response(prompt, st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    else:
        st.info("Your query does not seem related to the class content. Please ask about the class.")
