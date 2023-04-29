#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)

"""
if __name__ == "__main__":

import requests
import sys

repo = sys.argv[1]
owner = sys.argv[2]

url = f"https://api.github.com/repos/{owner}/{repo}/commits?author=rails"

response = requests.get(url)

if response.status_code == 200:
    commits = response.json()
    for commit in commits[:10]:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
else:
    print(f"Error: {response.status_code} - {response.reason}")

