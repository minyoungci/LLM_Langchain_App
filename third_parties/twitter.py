# tweepy -> 트위터 api 사용
# 링크드인 코드와 비슷함. 

import os
from datetime import datetime, timezone
import logging

import tweepy

logger = logging.getLogger("twitter")

auth = tweepy.OAuthHandler(
    os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_API_SECRET")
)
auth.set_access_token(
    os.environ.get("TWITTER_ACCESS_TOKEN"), os.environ.get("TWITTER_ACCESS_SECRET")
)
api = tweepy.API(auth)

def scrape_user_tweets(username, num_tweets=20):
    """
    Twitter 사용자의 원본 트윗 (즉, 리트윗이나 답글이 아닌)을 스크랩하고, 이를 사전의 목록으로 반환합니다.
    각 딕셔너리에는 세 개의 필드가 있습니다: "time_posted" (현재 시간 기준), "text", 그리고 "url
    """

    tweets = api.user_timeline(screen_name=username, count=num_tweets)

    tweet_list = []

    for tweet in tweets:
        if "RT @" not in tweet.text and not tweet.text.startswith("@"): # 실제 트윗, 리트윗 등 
            tweet_dict = {}
            tweet_dict["time_posted"] = str(
                datetime.now(timezone.utc) - tweet.created_at
            )
            tweet_dict["text"] = tweet.text
            tweet_dict[
                "url"
            ] = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
            tweet_list.append(tweet_dict)

    return tweet_list
