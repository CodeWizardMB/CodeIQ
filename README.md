# **CodeiQ: GitHub Code Analyzer with Gemini API**

CodeiQ connects **GitHub** repositories with **Gemini 1.5 API** to provide code analysis, error detection, and explanations. It helps developers easily debug their code, understand issues, and get detailed suggestions for improvement.

## **Features**
- **GitHub Integration**: Easily analyze public or private GitHub repositories.
- **Code Analysis**: Get real-time feedback and error detection.
- **Gemini API**: Leverages the **Gemini 1.5 API** to provide deep, context-aware insights and explanations of your code.

## **Setup Instructions**

### 1. **Clone the Repository**
To get started, first clone the repository to your local machine.

```bash
git clone https://github.com/your-username/codeiq.git
cd codeiq
```

### 2. **Install Dependencies**
Make sure you have **Python 3.8+** installed. Then, install the required libraries using pip.

```bash
pip install -r requirements.txt
```

### 3. **Get the Gemini API Key**
You need an API key from **Gemini 1.5** to use the code analysis features.

- Go to [Gemini 1.5 API page](https://www.example.com/gemini-api) and sign up.
- Once you’ve signed up, you’ll receive an API key.
- **Save the key** as you’ll need it in the next steps.

### 4. **Set Up GitHub Token**
In order to access GitHub repositories, you'll need a **GitHub token**.

- Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens).
- Click **Generate new token** and select the necessary permissions (repo access for private repositories).
- Copy and save the token.

### 5. **Configure API Keys in the Code**
Open the `main.py` file and add your **Gemini API Key** and **GitHub Token** to the configuration section:

```python
GEMINI_API_KEY = "your-gemini-api-key"
GITHUB_TOKEN = "your-github-token"
```

### 6. **Run the Application**

Now you’re ready to start the tool! In the terminal, run:

```bash
python main.py
```

### 7. **Using the Tool**
Once the app is running:
- Enter your **GitHub repository URL** when prompted.
- The tool will fetch the code, analyze it using the Gemini API, and provide detailed feedback on errors and suggestions for improvement.

## **How It Works**

1. **GitHub Integration**: The tool connects to GitHub via the GitHub API using your token, allowing access to your repositories.
2. **Code Analysis**: It fetches the code from the repository and sends it to the **Gemini 1.5 API** for analysis.
3. **Gemini Insights**: Gemini processes the code and provides real-time feedback, detecting errors and offering detailed explanations based on the long-context window feature.

## **Important Notes**
- Ensure your **GitHub token** has the appropriate permissions (e.g., `repo` scope for private repositories).
- The Gemini API has usage limits. Make sure you check their rate limits to avoid interruptions.

## **Contributing**
If you’d like to contribute to the project, feel free to fork the repository and submit a pull request. Please ensure your changes are well-documented.

## **License**
This project is licensed under the MIT License.

---

## **Links**
- **YouTube Video**: https://youtu.be/NE7MWEBtlmw
- **Website**:
- https://npqbbkp735sfoee5egtbfqww7v6n0pst.vercel.app/
- https://democodeiq.dora.run/
- https://baptistamerlin.wixstudio.com/codeiq

---
