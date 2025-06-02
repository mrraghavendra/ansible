import os

LOC = int(os.getenv("LINE_OF_CODE", "0"))
print(f"Line Of Code: {LOC}")

CopilotLOC = int(os.getenv("Copilot_LINE_OF_CODE", "0"))
print(f"Copilot Line Of Code: {CopilotLOC}")
