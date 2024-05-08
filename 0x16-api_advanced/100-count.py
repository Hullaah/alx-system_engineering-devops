#!/usr/bin/python3
"""This module contains recurse function
"""
import requests


def count_words(subreddit: str, word_list, word_counts=None, count=0, after=None):
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
    word_list = [x.lower() for x in word_list]
    word_counts = ({x: 0 for x in word_list}
                   if word_counts is None else word_counts)
    if response.status_code == 200:
        data = response.json()["data"]
        for k, _ in word_counts.items():
            for x in data["children"]:
                if k in x["data"]["title"].lower():
                    word_counts[k] += 1
        count += len(data["children"])
        sorted_word_counts_keys = sorted(word_counts, key=lambda k: word_counts[k])
        if data["after"] is None:
            for x in sorted_word_counts_keys:
                print(x+":", word_counts[x] * word_list.count(x))
            return
        count_words(subreddit, word_list, word_counts, count, data["after"])
    else:
        return None
