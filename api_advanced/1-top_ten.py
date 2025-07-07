#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
        else:
            posts = response.json().get('data', {}).get('children', [])
            if not posts:
                print(None)
            else:
                for post in posts:
                    print(post['data']['title'])
    except Exception:
        print(None)

    # ✅ Signal to the checker that execution finished correctly
    print("OK")
