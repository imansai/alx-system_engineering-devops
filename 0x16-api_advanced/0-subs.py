#!/usr/bin/python3
"""Function to get number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "alx.api.advanced/v1.0.0 (by /u/imannnnnnnnn)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
