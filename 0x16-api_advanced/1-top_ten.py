#!/usr/bin/python3
"""
This script provides a function to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for the given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'Custom User Agent'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for i, post in enumerate(posts):
                title = post['data']['title']
                print(f"{i + 1}. {title}")
        else:
            print("No hot posts found.")
    else:
        print("Invalid subreddit or API request failed.")

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    top_ten(subreddit)

