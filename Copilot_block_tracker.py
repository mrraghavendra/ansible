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
copilot_line_count = 0
non_copilot_line_count = 0

for line in added_lines:
    if '# Copilot start' in line:
        in_copilot_block = True
        continue
    elif '# Copilot end' in line:
        in_copilot_block = False
        continue

    if in_copilot_block:
        copilot_line_count += 1

# Filter only comment lines (Python-style comments)
comment_lines = [line for line in added_lines if '#' in line]

# (Optional) Filter if comments look like Copilot (heuristic, customizable)
copilot_like = [line for line in comment_lines if 'copilot' in line.lower()]

# Total lines to eleminate, look like Copilot.
non_copilot_line_count = len(added_lines) - len(copilot_like)

print("\nTotal added comment lines:", len(comment_lines))
print("\nLikely Copilot-generated comment lines:", len(copilot_like))
# print("\nExample lines:\n", "\n".join(copilot_like[:5]))
print("\nTotal Lines of Code:", non_copilot_line_count)
print("\nTotal Copilot added lines:", copilot_line_count)
