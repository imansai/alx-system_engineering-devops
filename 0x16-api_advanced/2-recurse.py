#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot/.json?after={after}"
    
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
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        print(f"Error: {response.status_code}")
        return None
