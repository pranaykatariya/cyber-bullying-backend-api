import threading
import time
import tweepy
from tweepy import OAuthHandler
import requests
import re

exitFlag = 0

class myThread (threading.Thread):
    


    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
   
    def run(self):


        def call(tweet):
            resp = requests.get('https://elit-hack.herokuapp.com/?query='+tweet)
            prediction = float(resp.text)
            print(prediction)

            if resp.status_code != 200:
            # This means something went wrong.
                raise ApiError('GET /tasks/ {}'.format(resp.status_code))

            return prediction
		
		# set up api keys
        consumer_key = 'SfsaCGMCXTULoYbvtk7jbn8Ga'
        consumer_secret = 'AuOabvc8CPQ9fscsz0Bg4yAjkFSpPJnLxR5DY8cnsLudrpfO78'
        access_token = '1222767616403501057-2lIofN7Q2Vyto4MxcdiPdkJyPsANjC'
        access_secret = 'X6TonNwsDB3tYKRqI6SDvK8yVwlaqmiXa2mVWsFIVkRn2'
		






		# set up auth and api
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)


        for status in tweepy.Cursor(api.home_timeline,exclude_replies=True).items(6):
            #print ("tweet: "+ status.text.encode('utf-8'))
            # get rid of punctuation
            tweet_id = status.id
            tweet = status.text
            tweet = tweet.lower()
            
            prediction = call(tweet)
            me = api.me()
            result = re.findall("@([a-zA-Z0-9]{1,15})", tweet)
            #print(result)
            url = 'https://cyber-bullying-report.herokuapp.com/api/task-create/'
            email_url ='http://cyber-bullying-report.herokuapp.com/api/sendmail/1'
            if prediction>0.5:
                print ("bullying")
                print (tweet)
                from_user_id = status.author.screen_name
                from_user = status.author.name
                to_user_id = result
                to_user = result
                location_me = me.location
                location_bully = status.user.location
                time_created = status.created_at
                details_object = {'from_user':from_user,
                                'to_user':to_user,
                                'title':tweet,
                                'completed':location_bully,
                                'bully_rate':prediction,
                                'platform':'twitter',
                                'time_now':time_created}
                email_object = {'from_user':from_user,
                                'from_user_id':from_user_id,
                                'to_user':to_user,
                                'to_user_id':to_user_id,
                                'bully_tweet':tweet,
                                'location_bully':location_bully,
                                'location_me':location_me,
                                'bully_rate':prediction,
                                'time_now':time_created,
                                'to':'pratikbansode2@gmail.com'}
                requests.post(url = url, data = details_object)
                #requests.post(url = email_url,data = email_object)
                #api.update_status("@" + status.author.screen_name+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)",in_reply_to_status_id= tweet_id)
            else:
                print ("not bullying")
                print(tweet)
                #api.update_status("@" + status.author.screen_name+"\n Good job, you're not a bully! (I am a bot in testing, don't take this too seriously)", in_reply_to_status_id= tweet_id)


def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
# thread2.start()

print ("Exiting Main Thread")
