#!/usr/bin/python3
"""
This script provides a recursive function to query the Reddit API and return a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for the given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store hot article titles. Defaults to None.
        after (str, optional): Parameter used for pagination. Defaults to None.
        
    Returns:
        list: List containing titles of all hot articles for the given subreddit.
    """
    if hot_list is None:
        hot_list = []
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
        
    headers = {
        'User-Agent': 'Custom User Agent'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    hot_articles = recurse(subreddit)
    
    if hot_articles is not None:
        print("Titles of hot articles:")
        for i, title in enumerate(hot_articles):
            print(f"{i + 1}. {title}")
    else:
        print("Invalid subreddit or no hot articles found.")

