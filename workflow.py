import requests
import os 

# === CONFIG ===
OWNER = "7nikhilkamboj"
REPO = "Gitsecrets"
WORKFLOW_FILE = "main.yml"  # name of your workflow file in .github/workflows
TOKEN = os.getenv("TOKEN") # your GitHub personal access token for workflows

url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_FILE}/dispatches"

# === PAYLOAD ===
data = {
    "ref": "main"  # or whatever your default branch is
}

# === TRIGGER ===
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 204:
    print("✅ Workflow triggered successfully!")
else:
    print("❌ Failed to trigger workflow:", response.status_code, response.text)
