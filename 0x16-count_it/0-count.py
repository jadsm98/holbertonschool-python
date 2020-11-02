#!/usr/bin/python3
""" Module"""

import requests

hot_l = []


def count_words(subreddit, word_list, count=0, after=None):

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return

    for child in sub_info.json().get("data").get("children"):
        for i in word_list:
            if i in child.get("data").get("title").split(' ') or \
                    i.capitalize() in child.get("data").get("title").split(' '):

                for j in range(child.get("data").get("title").split(' ').count(i) + 
                               child.get("data").get("title").split(' ').count(i.capitalize())):
                    hot_l.append(i)

    info = sub_info.json()
    if not info.get("data").get("after"):
        for i in word_list:
            if hot_l.count(i) != 0:
                print('{}: {}'.format(i, hot_l.count(i)))
        return

    return count_words(subreddit, word_list, info.get("data").get("count"),
                       info.get("data").get("after"))
