import tweepy
from tweepy import OAuthHandler, StreamListener
import json


def get_hashtag():
    consumer_key = 'NFbD1D02Zcpiycf3R4ERNHVZT'
    consumer_secret = 'gudVy9WtPFg5zM1vKD2gHMHrWCU6iZqVpRnRqDRYBdtFbSUYbQ'
    access_token = '964918233391300609-0cnIOmL24ffvyQVd2M3IYNj01L6fUlp'
    access_token_secret = '7IGEGg6c1lE14KIYcAIkomCSECXhL9NUxvoYRTGX2Avb5'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    pakistan_WOE_ID = 2211096

    pakistan_trends = api.trends_place(pakistan_WOE_ID)
    trends = json.loads(json.dumps(pakistan_trends, indent=4))
    objects = []
    for trend in trends[0]["trends"]:
        objects.append(trend)
    return objects
