import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
import requests

# Load .env variables
load_dotenv()
GITHUB_TOKEN = "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"
API_KEY = "AIzaSyBKsBD_gUqp90DbOvW9j_66oyQK-XeoBeY"

# Configure API
genai.configure(api_key=API_KEY)
model = genai.models.list_models()[0]  # Ensure model availability

def gemini_chat(message, history):
    try:
        response = genai.generate_text(prompt=message)
        assistant_response = response.generations[0]["text"]
    except Exception as e:
        assistant_response = f"Error: {str(e)}"
    history.append((message, assistant_response))
    return history, history

def analyze_github_and_ask(repo_url, question):
    if not repo_url.startswith("https://github.com/"):
        return "Invalid GitHub repository URL."
    try:
        owner, repo = repo_url.split("https://github.com/")[1].split("/")[:2]
        repo_api = f"https://api.github.com/repos/{owner}/{repo}"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        repo_resp = requests.get(repo_api, headers=headers)
        lang_resp = requests.get(f"{repo_api}/languages", headers=headers)
        if repo_resp.status_code != 200:
            return f"Error: {repo_resp.status_code}"
        repo_data = repo_resp.json()
        languages = ', '.join(lang_resp.json().keys()) if lang_resp.status_code == 200 else "Unavailable"
        context = f"Repo: {repo_data['html_url']}\nDescription: {repo_data['description']}\nLanguages: {languages}"
        return gemini_chat_with_context(context, question)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    with gr.Blocks() as demo:
        with gr.Tab("Chat"):
            chatbot = gr.Chatbot()
            msg = gr.Textbox()
            btn = gr.Button("Send")
            history = gr.State([])
            btn.click(gemini_chat, [msg, history], [chatbot, history])
        with gr.Tab("GitHub"):
            url = gr.Textbox()
            qst = gr.Textbox()
            out = gr.Textbox()
            btn = gr.Button("Analyze")
            btn.click(analyze_github_and_ask, [url, qst], out)
    demo.launch()

