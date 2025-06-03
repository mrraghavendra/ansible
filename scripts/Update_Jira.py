import os

LOC = int(os.getenv("LINES_OF_CODE", "0"))
print(f"Line Of Code: {LOC}")

CopilotLOC = int(os.getenv("COPILOT_LINES_OF_CODE", "0"))
print(f"Copilot Line Of Code: {CopilotLOC}")
