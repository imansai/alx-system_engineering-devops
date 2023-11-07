#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of keywords to count in the post titles.
        counts (dict, optional): A dictionary to store the counts of keywords.
            Defaults to None.
        after (str, optional): The ID of the last post in the current batch.
            Defaults to None.

    Returns:
        None: This function does not return any value. It prints the results.

    Note:
        - The function works recursively and counts keywords in hot articles' titles.
        - The results are printed in descending order by count and then sorted alphabetically.
        - Words with no matches are skipped and not printed.
        - Invalid subreddits may return a redirect to search results. No results are printed in this case.
    """
    if counts is None:
        counts = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot/.json?after={after}"

    headers = {
        "User-Agent": "alx.api.advanced:v1.0.0 (by /u/imannnnnnnnn)"
    }

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
