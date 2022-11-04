#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ if not valid subreddit, it prints None """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'arsi_gebre'}
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 404:
        print(None)
        return None

    try:
        data = response.json().get("data")
        children = data.get("children")
        for child in children[:10]:
            post = child.get("data")
            print(post.get("title"))
    except ValueError:
        print(None)
        return None
