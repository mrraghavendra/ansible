import os
import subprocess

LOC = int(os.getenv("LINES_OF_CODE", "0"))
print(f"Line Of Code: {LOC}")

CopilotLOC = int(os.getenv("COPILOT_LINES_OF_CODE", "0"))
print(f"Copilot Line Of Code: {CopilotLOC}")

result = subprocess.run(["git", "symbolic-ref", "--short", "HEAD"], capture_output=True, text=True)
branch_name = result.stdout.strip()

print(f"Current branch 1: {branch_name}")
