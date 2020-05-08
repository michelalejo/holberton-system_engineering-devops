#!/usr/bin/python3
"""recursive function that queries the Reddit API,
returns a list containing the titles of all hot articles"""

import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=""):
    if after is None:
        return []

    info = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    info += "?limit=100&after={}".format(after)
    headers = {'user-agent': 'request'}
    data = requests.get(info, headers=headers,
                        allow_redirects=False)
    if str(data) == "<Response [200]>":
        dat = data.json()
        hot_posts_json = dat.get("data").get("children")
        for post in hot_posts_json:
            hot_list.append(post.get("data").get("title"))
        return hot_list + recurse(subreddit, [], dat.get("data").get("after"))
    else:
        return None
