#!/usr/bin/python3
"""
Takes in a github user name and a repository name
and list the recent 10 commits
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(argv[2], argv[1]))
    r_dict = r.json()
    for commit in r_dict[:10]:
        print("{}: {}"
              .format(commit.get('sha'),
                      commit.get('commit').get('author').get('name')))
