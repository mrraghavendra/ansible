import subprocess
import os
import re
import requests

LOC = int(os.getenv("LINES_OF_CODE", "0"))
print(f"Line Of Code: {LOC}")

CopilotLOC = int(os.getenv("COPILOT_LINES_OF_CODE", "0"))
print(f"Copilot Line Of Code: {CopilotLOC}")

# Get Branch name from built in enc variables
branch = os.environ.get('GITHUB_HEAD_REF', '') or os.environ.get("GITHUB_REF", "")

# If you want just the branch name:
if branch.startswith("refs/heads/"):
    branch = branch.replace("refs/heads/", "")

print(f"Branch Name: {branch}")

# Extract Jira issue key (e.g., "ABC-123") from branch
match = re.search(r'([A-Z]+-\d+)', branch)
if not match:
    print("No Jira issue key found in branch name.")
    exit(1)

issue_key = match.group(1)
print(f"Issue Key Detected: {issue_key}")

# ******************* Update JIRA ****************************************
JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")

# Jira API endpoint
url = f"https://{JIRA_DOMAIN}/rest/api/2/issue/{issue_key}"

# Payload to update custom field
payload = {
    "fields": {
        "customfield_33491": 10,
        "customfield_19938":[ { "value": "GitHub Co-Pilot" } ]
    }
}

# Headers and Auth
headers = { "Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " }

if CopilotLOC > 0:
    # Check if issue exists
    get_url = f"{url}/rest/api/2/issue/{issue_key}"
    get_response = requests.get(get_url, headers=headers)
    
    if get_response.status_code == 200:
        print(f"Issue {issue_key} exists. Proceeding with update...")    
        response = requests.put(url, json=payload, headers=headers)
        if response.status_code == 204:
            print(f"Successfully updated Jira issue: {issue_key}")
        else:
            print(f"Failed to update Jira: {response.status_code} - {response.text}")
    else:
        print(f"Issue {issue_key} not found. Status: {get_response.status_code}")
else:
    print("No CopilotLOC changes detected, skipping Jira update.")
