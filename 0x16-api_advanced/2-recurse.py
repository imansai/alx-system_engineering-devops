#!/usr/bin/python3
"""Function that gets titles of all hot posts on a given subreddit."""

import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "alx.api.advanced/v.1.0.0 (by /u/imannnnnnnnn)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        print(f"Error: {response.status_code}")
        return None
