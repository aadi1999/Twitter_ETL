import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "QwUGV94DkiDXdcoLRXEG7nBjZ"
access_secret = "pACSUQKuwFn5QuebdGFQsNyXx0D7S42M65BslYECUudH01W9KR"
consumer_key = "887360447111766017-ffgMXPzJpNk3MVmr6B1b2OdWuQ4Nltk"
consumer_secret = "8pAUxp0aR9JVEa9YZmVGgVrjRkftGVgfNa2SxJJ04nKvK"

#Twitter authentication : to create the connection between current code and twitter api, using tweepy
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key,consumer_secret)

#Creating the API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = "@elonmusk",
                           # 200 is the maximum count allowed, like how many tweets you want extract
                           # from that particular timeline
                           count = 200,
                           include_rts = False,
                           #Necessary to keep full_text
                           #otherwise only the firrst 140 words are extracted
                           tweet_mode = 'extended'

                           )
# print(tweets)

# f = open("output.txt", "a")
# print(tweets, file=f)
#
# f.close()



tweet_list = []
for tweet in tweets:
    text  = tweet._json["full_text"]

    refined_tweet = {
        "user":tweet.user.screen_name,
        'text': text,
        "favorite_count": tweet.favorite_count,
        "retweet_count":tweet.retweet_count,
        "created_at": tweet.created_at,
    }
    tweet_list.append(refined_tweet)
    # print(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv("elonmusk_twitter_data.csv") #saving the data in the csv file