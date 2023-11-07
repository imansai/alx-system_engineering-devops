#!/usr/bin/python3
"""Function that gives wordcount of hot posts on a subreddit."""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries API and prints wordcount of articles in a subreddit.

    Args:
        subreddit (str): Name of the subreddit to search.
        word_list (list): List of words to count in the post titles.
        counts (dict, optional): Dictionary to store the counts of keywords.
        after (str, optional): ID of the last post in the current batch.
    """
    if counts is None:
        counts = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot/.json?after={after}"

    headers = {"User-Agent": "alx.api.advanced:v1.0.0 (by /u/imannnnnnnnn)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if title.count(word) > 0:
                    counts[word] = counts.get(word, 0) + title.count(word)

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, counts, after)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    elif response.status_code == 404:
        print("Invalid subreddit.")
    else:
        print(f"Error: {response.status_code}")
