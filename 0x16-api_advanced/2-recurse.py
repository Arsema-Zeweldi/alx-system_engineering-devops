#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """if not a valid subreddit, return None """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'arsi_gebre'}
    parameters = {
        'limit': 100,
        'after': after
    }
    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)

    if after is None:
        return hot_list

    if response.status_code != 200:
        return None

    try:
        JSON = response.json()
    except ValueError:
        return None

    try:
        data = JSON.get("data")
        after = data.get("after")
        titles = data.get("children")
        for title in titles:
            post = title.get("data")
            hot_list.append(post.get("title"))

    except:
        return None

    return recurse(subreddit, hot_list, after)
