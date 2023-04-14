import requests
import json

# GitHub API token
TOKEN = "your_github_api_token_here"

# Repository information
owner = "repository_owner"
repo = "repository_name"

# URL for getting all the pull requests
url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

# Get all the pull requests
response = requests.get(url, headers={"Authorization": f"Bearer {TOKEN}"})

if response.status_code == 200:
    pull_requests = json.loads(response.content)

    # Loop through all the pull requests and close them
    for pull_request in pull_requests:
        pr_number = pull_request["number"]
        close_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
        close_payload = {"state": "closed"}

        close_response = requests.patch(
            close_url, headers={"Authorization": f"Bearer {TOKEN}"}, json=close_payload
        )

        if close_response.status_code == 200:
            print(f"Closed PR #{pr_number}")
        else:
            print(f"Failed to close PR #{pr_number}")
else:
    print("Failed to get pull requests")
