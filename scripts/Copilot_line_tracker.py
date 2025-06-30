import subprocess

# Get the diff for the PR: lines added (starting with '+')
result = subprocess.run(['git', 'diff', 'origin/master...HEAD'], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE, 
                        text=True)

if result.returncode != 0:
    print("Git error:", result.stderr)
else:
    print("Git out:", result.stdout)
    added_lines = [
        line for line in result.stdout.splitlines()
        if line.startswith('+') and not line.startswith('+++')  # Exclude diff metadata
    ]

    # Filter only comment lines (Python-style comments)
    comment_lines = [line for line in added_lines if '#' in line]

    # (Optional) Filter if comments look like Copilot (heuristic, customizable)
    copilot_like = [line for line in comment_lines if 'copilot' in line.lower()]

    print("Total added comment lines:", len(comment_lines))
    print("Likely Copilot-generated comment lines:", len(copilot_like))
    print("\nExample lines:\n", "\n".join(copilot_like[:5]))
