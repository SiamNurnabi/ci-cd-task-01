import requests

# Define the repository 
repo = "openai/openai-cookbook"
url = f"https://api.github.com/repos/{repo}/commits"

# Fetch commits
response = requests.get(url)
if response.status_code == 200:
    commits = response.json()
    for commit in commits: 
        print(f"Commit: {commit.hexsha}\nMessage: {commit.message.strip()}\n")
else:
    print(f"Error: {response.status_code}")