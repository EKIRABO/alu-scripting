#!/usr/bin/python3
""" Print the titles of the first 10 Hot Posts."
import requests


def top_ten(subreddit):
    """ Prints titles of first 10 hot posts """
    headers = {'User-Agent': 'Me:05'}
    url = "https://reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
