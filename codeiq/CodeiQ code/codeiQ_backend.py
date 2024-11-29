import os
import google.generativeai as genai
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please configure your environment variables.")
genai.configure(api_key=GEMINI_API_KEY)

# GitHub Token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN is not set. Please configure your environment variables.")

def gemini_chat(message, history):
    """
    Handles general chat messages with Gemini and updates the chat history.
    """
    gemini_history = [{"role": "user", "parts": [msg]} for msg, _ in history]
    gemini_history.append({"role": "user", "parts": [message]})

    try:
        response = genai.GenerativeModel('gemini-pro').generate_content(gemini_history)
        assistant_response = response.text
    except Exception as e:
        assistant_response = f"Error: {str(e)}"

    history.append((message, assistant_response))
    return history, history

def gemini_chat_with_context(context, question):
    """
    Combines context (GitHub data) with the user's question and generates a response.
    """
    gemini_history = [
        {"role": "user", "parts": [f"Context: {context}"]},
        {"role": "user", "parts": [question]}
    ]
    try:
        response = genai.GenerativeModel('gemini-pro').generate_content(gemini_history)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def analyze_github_and_ask(repo_url, question):
    """
    Fetches GitHub repository details and generates an answer using Gemini API.
    """
    if not repo_url.startswith("https://github.com/"):
        return "Invalid GitHub repository URL."

    try:
        owner, repo_name = repo_url.split("https://github.com/")[1].split("/")[:2]
    except ValueError:
        return "Invalid GitHub repository URL structure."

    github_api_url = f"https://api.github.com/repos/{owner}/{repo_name}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    try:
        response = requests.get(github_api_url, headers=headers)
        if response.status_code != 200:
            return f"Error: GitHub returned status code {response.status_code}."

        repo_data = response.json()
        description = repo_data.get("description", "No description provided.")
        languages = repo_data.get("language", "Unknown")
        context = f"GitHub Repository: {repo_url}\nDescription: {description}\nPrimary Language: {languages}"
        return gemini_chat_with_context(context, question)
    except Exception as e:
        return f"Error accessing GitHub: {str(e)}"
