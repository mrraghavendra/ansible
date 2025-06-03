import os
import subprocess

# Get the diff for the PR: lines added (starting with '+')
result = subprocess.run(['git', 'diff', 'origin/master...HEAD'], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE, 
                        text=True)

if result.returncode != 0:
    print("Git error:", result.stderr)
else:
    added_lines = [
        line for line in result.stdout.splitlines()
        if line.startswith('+') and not line.startswith('+++')  # Exclude diff metadata
    ]


in_copilot_block = False
copilot_lines_count = 0

for line in added_lines:
    if '# Copilot start' in line:
        in_copilot_block = True
        continue
    elif '# Copilot end' in line:
        in_copilot_block = False
        continue

    if in_copilot_block:
        copilot_lines_count += 1

# Filter only comment lines (Python-style comments)
comment_lines = [line for line in added_lines if '#' in line]

# (Optional) Filter if comments look like Copilot (heuristic, customizable)
copilot_like = [line for line in comment_lines if 'copilot' in line.lower()]

# print("\nTotal added comment lines:", len(comment_lines))
# print("\nLikely Copilot-generated comment lines:", len(copilot_like))
# print("\nExample lines:\n", "\n".join(copilot_like[:5]))
# Write to GitHub Actions output
with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
  print(f"LinesOfCode={len(added_lines) - len(comment_lines)}", file=fh)
  print(f"CopilotLinesOfCode={copilot_lines_count}", file=fh)
