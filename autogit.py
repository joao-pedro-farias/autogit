from pathlib import Path
import subprocess

current_directory = Path.cwd()

if (current_directory / '.git').is_dir():
    print("Directory is already a git repository")
else:
    print("Initializing git repository")
    subprocess.run(['git', 'init'], check=True)

response = input("Do you want to upload files to git? (y/n): ")

if response.lower() == 'y':
    print("Uploading")
    subprocess.run(['git', 'add', '.'])

    commit = input("Enter commit message (press Enter for auto commit): ")
    if commit.strip() == "":
        print("Automatic commit")
        subprocess.run(['git', 'commit', '-m', 'auto commit'])
    else:
        print("Your commit message:", commit)
        subprocess.run(['git', 'commit', '-m', commit])

    url = input("Paste the repository URL here: ")
    result = subprocess.run(
        ['git', 'remote'],
        capture_output=True,
        text=True
    )
    if 'origin' in result.stdout:
        subprocess.run(['git', 'remote', 'set-url','origin', url])
    else:
        subprocess.run(['git', 'remote', 'add', 'origin', url])


    branch = input("Enter branch name (press Enter for main): ")
    if branch.strip() == "":
        print("Pushing to branch main")
        subprocess.run(['git', 'branch', '-M', 'main'])
        subprocess.run(['git', 'push', '-u', 'origin', 'main'])
    else:
        print("Pushing to branch", branch)
        subprocess.run(['git', 'branch', '-M', branch])
        subprocess.run(['git', 'push', '-u', 'origin', branch])
