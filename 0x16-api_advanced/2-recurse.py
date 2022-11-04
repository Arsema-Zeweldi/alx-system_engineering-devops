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

    if response.status_code == 200:
        data = response.json().get("data").get("after")
        if data is not None:
            after = response.json().get("after")
            recurse(subreddit, hot_list)
        list_titles = response.json().get("data").get("children")
        for title in list_titles:
            hot_list.append(title.get('data').get("title"))
        return hot_list
    else:
        return (None)
