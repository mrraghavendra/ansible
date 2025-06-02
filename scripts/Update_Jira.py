import os

LOC = int(os.getenv("LOC", "0"))
print(f"Line Of Code: {LOC}")

CopilotLOC = int(os.getenv("CopilotLOC", "0"))
print(f"Copilot Line Of Code: {CopilotLOC}")
