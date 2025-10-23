import os, glob
from dotenv import load_dotenv
import google.generativeai as genai
from github import Github

# Load environment variables from .env file
load_dotenv()

# Access keys from environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gh = Github(os.getenv("GITHUB_TOKEN"))
repo_name = os.getenv("GITHUB_REPOSITORY")
repo = gh.get_repo(repo_name)

model = genai.GenerativeModel("gemini-1.5-pro")

def analyze_file(file_path):
    try:
        with open(file_path, "r", errors="ignore") as f:
            content = f.read()

        prompt = f"""
        You are a professional code reviewer.
        Analyze this file and report:
        - Bugs or potential errors
        - Missing or unclear documentation
        - Code quality or performance issues
        Respond in the format:
        Title: <short summary>
        Body: <detailed description and suggestions>
        """

        response = model.generate_content(prompt + "\n\n" + content)
        text = response.text.strip()

        if "Title:" in text:
            title = text.split("Title:")[1].split("Body:")[0].strip()
            body = text.split("Body:")[1].strip()
            return title, body
    except Exception as e:
        print(f"⚠️ Error analyzing {file_path}: {e}")
    return None, None

for file_path in glob.glob("**/*.py", recursive=True):
    title, body = analyze_file(file_path)
    if title and body:
        repo.create_issue(title=title, body=body, labels=["AI-generated"])
        print(f"✅ Created issue for {file_path}: {title}")
