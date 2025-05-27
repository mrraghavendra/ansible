import subprocess

def get_diff_stats():
    # Get diff of current branch vs base
    result = subprocess.run(
        ['git', 'diff', '--numstat', 'mrraghavendra/ansible:master...HEAD'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    total_added = 0
    total_deleted = 0
    print(f"Inside PR Result" + result.stdout.strip())
    for line in result.stdout.strip().split('\n'):
        if line:
            added, deleted, file = line.split('\t')
            total_added += int(added)
            total_deleted += int(deleted)
    print(f"Total lines added: {total_added}")
    print(f"Total lines deleted: {total_deleted}")
  
if __name__ == "__main__":
    get_diff_stats()
