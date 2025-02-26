#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found, returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:2-recurse:v1.0 (by /u/Fantastic-Farmer4508)"
    }
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    posts = data.get("children")
    for post in posts:
        hot_list.append(post.get("data").get("title"))

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
