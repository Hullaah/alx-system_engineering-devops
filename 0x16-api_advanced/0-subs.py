#!/usr/bin/python3
"""This module contains the number_of_subscribers function
"""
import requests
import json


def number_of_subscribers(subreddit: str):
    """A function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.

    Args:
        subreddit: subreddit to get number of subscribers from

    Returns:
        int: number of subscribers
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    subreddit_data = json.loads(response.text)
    return (0 if "subscribers" not in subreddit_data["data"]
            else subreddit_data["data"]["subscribers"])
