import requests
def call(tweet):
    resp = requests.get('https://elit-hack.herokuapp.com/?query='+tweet)
    prediction = float(resp.text)

    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))

    if prediction>0.5:
        return 1
    else:
        return 0


import tweepy
from tweepy import OAuthHandler

# set up api keys
consumer_key = 'SfsaCGMCXTULoYbvtk7jbn8Ga'
consumer_secret = 'AuOabvc8CPQ9fscsz0Bg4yAjkFSpPJnLxR5DY8cnsLudrpfO78'
access_token = '1222767616403501057-2lIofN7Q2Vyto4MxcdiPdkJyPsANjC'
access_secret = 'X6TonNwsDB3tYKRqI6SDvK8yVwlaqmiXa2mVWsFIVkRn'


# set up auth and api
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

for status in tweepy.Cursor(api.home_timeline).items(1):
    print ("tweet: "+ status.text.encode('utf-8'))
    # get rid of punctuation
    tweet = status.text
    tweet = tweet.lower()
    if call(tweet):
        print ("bullying")
        api.update_status("@" + status.author.screen_name+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)", status.id)
    else:
        print ("not bullying")
        api.update_status("@" + status.author.screen_name+"\n Good job, you're not a bully! (I am a bot in testing, don't take this too seriously)", status.id)
