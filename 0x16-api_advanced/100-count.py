#!/usr/bin/python3
"""
A module that contains a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Parses the title of all hot articles and prints a sorted count of given keywords.
    """
    if count_dict is None:
        count_dict = {}
        for word in word_list:
            word = word.lower()
            if word not in count_dict:
                count_dict[word] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:100-count:v1.0 (by /u/Fantastic-Farmer4508)"
    }
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    posts = data.get("children")

    for post in posts:
        title = post.get("data").get("title").lower()
        for word in word_list:
            word = word.lower()

            split_title = [s for s in title.split() if s.isalnum()]

            for s in split_title:
                if s == word:
                    count_dict[word] += 1

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(),
                              key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return None
