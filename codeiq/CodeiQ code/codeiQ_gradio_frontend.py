import gradio as gr
from codeiQ_backend import gemini_chat, analyze_github_and_ask

# Gradio Interface
with gr.Blocks(title="CodeiQ - Your AI Coding Assistant") as demo:
    gr.Markdown("## Welcome to CodeiQ - Your AI Coding Assistant! 🎉")
    gr.Markdown("Ask questions, analyze GitHub repositories, and chat with me about coding.")

    # Chat Tab
    with gr.Tab("Chat with CodeiQ"):
        chatbot = gr.Chatbot(label="CodeiQ Chat", height=300)
        message_box = gr.Textbox(placeholder="Ask CodeiQ something...", label="Your Message")
        submit_button = gr.Button("Send")
        history_state = gr.State([])  # To maintain chat history

        submit_button.click(
            gemini_chat,
            inputs=[message_box, history_state],
            outputs=[chatbot, history_state]
        )

    # GitHub Repository Analysis Tab
    with gr.Tab("GitHub Repository Analysis"):
        repo_url = gr.Textbox(placeholder="Enter a GitHub repository URL", label="GitHub Repository URL")
        repo_question = gr.Textbox(placeholder="Ask a question related to the repository", label="Your Question")
        repo_submit = gr.Button("Submit and Analyze")
        repo_output = gr.Textbox(label="Answer")

        repo_submit.click(
            analyze_github_and_ask,
            inputs=[repo_url, repo_question],
            outputs=repo_output
        )

# Launch Gradio App
if __name__ == "__main__":
    demo.launch()
