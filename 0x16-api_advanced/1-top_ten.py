#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:1-top_ten:v1.0 (by /u/Fantastic-Farmer4508)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data").get("children")
        for post in data:
            print(post.get("data").get("title"))
    else:
        print(None)
