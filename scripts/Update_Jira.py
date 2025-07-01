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

# ******************* Update JIRA ****************************************
JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
custom_field_id = "customfield_10042"  # Replace with your actual custom field ID

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
