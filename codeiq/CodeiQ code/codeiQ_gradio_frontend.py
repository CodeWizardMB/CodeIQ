import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Set up the Gemini API
# Replace placeholders with provided API keys
genai.configure(api_key="AIzaSyBKsBD_gUqp90DbOvW9j_66oyQK-XeoBeY")
model = genai.GenerativeModel('gemini-pro')

# GitHub Token
GITHUB_TOKEN = "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"


def gemini_chat(message, history):
    """
    Handles general chat messages with Gemini and updates the chat history.
    """
    gemini_history = [{"role": "user", "parts": [msg]} for msg, _ in history]
    gemini_history.append({"role": "user", "parts": [message]})

    try:
        response = model.generate_content(gemini_history)
        assistant_response = response.text
    except Exception as e:
        assistant_response = f"Error: {str(e)}"

    # Update history with the new message and response
    history.append((message, assistant_response))
    return history, history

def analyze_github_and_ask(repo_url, question):
    """
    Validates the GitHub URL, fetches repository details, and generates an answer
    to the question using the Gemini API, authenticated with a GitHub token.
    """
    if not repo_url.startswith("https://github.com/"):
        return "Invalid GitHub repository URL. Please provide a valid URL."

    # Extract the repository owner and name
    repo_parts = repo_url.split("https://github.com/")[1].split("/")
    owner, repo_name = repo_parts[0], repo_parts[1]

    # GitHub API URL for repository details
    github_api_url = f"https://api.github.com/repos/{owner}/{repo_name}"

    try:
        # Make a request to the GitHub API with the token for authentication
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        response = requests.get(github_api_url, headers=headers)

        if response.status_code != 200:
            return f"Failed to access the repository. Status code: {response.status_code}"

        repo_data = response.json()
        context = f"GitHub repository: {repo_url}\nDescription: {repo_data['description']}\nLanguages: {repo_data['language']}"
        
        # Use the gemini_chat_with_context function to get the response
        return gemini_chat_with_context(context, question)
    
    except Exception as e:
        return f"Error accessing the repository: {str(e)}"

def gemini_chat_with_context(context, question):
    """
    Combines the provided context (GitHub or file) with the user's question
    and generates a response using the Gemini API.
    """
    gemini_history = [
        {"role": "user", "parts": [f"Context: {context}"]},
        {"role": "user", "parts": [question]}
    ]
    
    try:
        response = model.generate_content(gemini_history)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface Setup
with gr.Blocks(title="CodeiQ - Your AI Coding Assistant", theme=gr.themes.Soft(primary_hue="purple", secondary_hue="blue")) as demo:
    gr.Markdown(
        """
        # Welcome to CodeiQ - Your AI Coding Assistant! 🚀
        Ask questions, analyze GitHub repositories, and chat about coding.
        """
    )
    
    with gr.Tab("Chat with CodeiQ"):
        chatbot = gr.Chatbot(label="CodeiQ Chat", height=400)
        message_box = gr.Textbox(placeholder="Ask CodeiQ something...", label="Your Message")
        submit_button = gr.Button("Send", variant="primary")

        submit_button.click(
            gemini_chat,
            inputs=[message_box, chatbot],
            outputs=[chatbot, chatbot]
        )

    with gr.Tab("GitHub Repository Analysis"):
        repo_url = gr.Textbox(placeholder="Enter a GitHub repository URL", label="GitHub Repository URL")
        repo_question = gr.Textbox(placeholder="Ask a question related to the repository", label="Your Question")
        repo_submit = gr.Button("Submit and Analyze", variant="primary")
        repo_output = gr.Textbox(label="Answer")

        repo_submit.click(
            analyze_github_and_ask,
            inputs=[repo_url, repo_question],
            outputs=repo_output
        )

    gr.Markdown(
        """
        ### Powered by AI and GitHub
        © 2024 CodeiQ. All rights reserved.
        """
    )

demo.launch(server_name="127.0.0.1", server_port=8080)

