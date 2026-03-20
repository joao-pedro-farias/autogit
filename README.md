# AutoGit - Git Automation with Python

A simple Python script that automates the process of initializing, committing, and pushing a project to GitHub directly from the terminal.

## Features

- Checks if the current directory is already a Git repository
- Initializes Git automatically (`git init`)
- Adds all files (`git add .`)
- Creates a commit (custom or automatic message)
- Connects to a remote repository
- Allows branch selection
- Pushes code to GitHub

## How it works

The script executes Git commands using Python (`subprocess`), replicating a real development workflow in the terminal.

## Technologies

- Python
- Git
- pathlib
- subprocess

## Usage

1. Clone or download the project

```bash
git clone https://github.com/joao-pedro-farias/autogit.git
cd autogit
```
2. Run the script:

```bash
python3 autogit.py
