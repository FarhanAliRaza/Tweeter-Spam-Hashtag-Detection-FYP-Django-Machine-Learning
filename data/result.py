import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)


def get_hashtag():
    with open(os.path.join(BASE_DIR, 'result.txt'), encoding='utf-8') as json_file:
        hashtag = json.load(json_file)
    for obj in hashtag:
        return obj


def get_spam_tweets():
    with open(os.path.join(BASE_DIR, 'spam_tweets.txt'), encoding='utf-8') as json_file:
        tweets = json.load(json_file)
    return tweets
