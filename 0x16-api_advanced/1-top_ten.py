#!/usr/bin/python3
"""This module contains top_ten function
"""
import requests
import json


def top_ten(subreddit: str):
    """A function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit: subreddit to get top ten posts from

    Returns:
        None
    """
    payload, headers = {"limit": "10"}, {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = requests.get(url, params=payload,
                            headers=headers, allow_redirects=False)
    try:
        top_posts = json.loads(response.text)["data"]["children"]
        for x in top_posts:
            print(x["data"]["title"])
    except KeyError:
        print(None)
