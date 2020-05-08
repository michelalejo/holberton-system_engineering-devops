#!/usr/bin/python3
"""Function that queries Reddit API and prints the titles 10 first hot posts"""


import requests
from sys import argv


def top_ten(subreddit):
    """Function that queries Reddit API,
    prints the titles 10 first hot posts"""
    info = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    info += "?limit=10"
    headers = {'user-agent': 'request'}
    data = requests.get(info, headers=headers,
                        allow_redirects=False)
    if str(data) == "<Response [200]>":
        data_json = data.json()
        hot_posts_data_json = data_json.get("data").get("children")
        top_10_posts = ""
        for post in hot_posts_data_json:
            top_10_posts += post.get("data").get("title") + "\n"
        print(top_10_posts, end="")
    else:
        print(None)
        return
