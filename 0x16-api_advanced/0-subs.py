#!/usr/bin/python3
"""
This script provides a function to query the Reddit API and retrieve the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for the given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: Number of subscribers for the subreddit. Returns 0 for invalid subreddits.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Custom User Agent'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    subscribers_count = number_of_subscribers(subreddit)
    print(f"Number of subscribers in r/{subreddit}: {subscribers_count}")

