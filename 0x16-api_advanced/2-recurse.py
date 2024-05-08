#!/usr/bin/python3
"""This module contains recurse function
"""
import requests


def recurse(subreddit: str, hot_list=[], count=0, after=None):
    """A function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit: subreddit to get hot posts from
        hot_list: the list of hottest posts so far
        count: the number of items already seen in the listing.
                it is used to paginate the api
        after: the token used to paginate the api
    Returns:
        None
    """
    headers, payload = {
        "User-Agent": "Mozilla/5.0"}, {"count": count, "after": after}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = requests.get(url, params=payload,
                            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]
        hot_list += [x["data"]["title"] for x in data["children"]]
        count += len(data["children"])
        if data["after"] is None:
            return hot_list
        return recurse(subreddit, hot_list, count, data["after"])
    else:
        return None
