import os
import subprocess

LOC = int(os.getenv("LINES_OF_CODE", "0"))
print(f"Line Of Code: {LOC}")

CopilotLOC = int(os.getenv("COPILOT_LINES_OF_CODE", "0"))
print(f"Copilot Line Of Code: {CopilotLOC}")

resultBranch_name = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
branch_name = resultBranch_name.stdout.strip()

print(f"Current branch 1: {branch_name}")
