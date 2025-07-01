import os
import subprocess

LOC = int(os.getenv("LINES_OF_CODE", "0"))
print(f"Line Of Code: {LOC}")

CopilotLOC = int(os.getenv("COPILOT_LINES_OF_CODE", "0"))
print(f"Copilot Line Of Code: {CopilotLOC}")

branch = os.environ.get('GITHUB_HEAD_REF', '') or os.environ.get("GITHUB_REF", "")

print(f"GITHUB_REF: {github_ref}")

# If you want just the branch name:
if branch.startswith("refs/heads/"):
    branch = branch.replace("refs/heads/", "")

print(f"Branch Name: {branch}")
