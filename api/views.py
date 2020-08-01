from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task, Admin_Messages

from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.conf import settings

import tweepy
import threading
import time
from tweepy import OAuthHandler
import requests

import re
import json
# Create your views here.

def hashtagTwitter(request):
	
	if request.method == "POST":
		hash = request.POST['hash']
		hash = str(hash)
		
		if hash.startswith('#'):
			pass
		else:
			hash = '#'+hash

		exitFlag = 0

		class myThread (threading.Thread):
			


			def __init__(self, threadID, name, counter):
				threading.Thread.__init__(self)
				self.threadID = threadID
				self.name = name
				self.counter = counter
		
			def run(self):
				# hash = "#government"
				print(hash)


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


				for status in tweepy.Cursor(api.search,q=hash,
											# geocode="22.3511148,78.6677428,1000000km",
										lang="en").items(2):
					#print ("tweet: "+ status.text.encode('utf-8'))
					# get rid of punctuation
					tweet_id = status.id
					tweet = status.text
					tweet = tweet.lower()
					print(tweet)
					
					prediction = call(tweet)
					me = api.me()
					result = re.findall("@([a-zA-Z0-9]{1,15})", tweet)
					print(result)
					url = 'https://cyber-bullying-report.herokuapp.com/api/task-create/'
					email_url ='http://cyber-bullying-report.herokuapp.com/api/sendmail/1'
					if prediction>0.5:
						print ("bullying")
						print (tweet)
						from_user_id = status.author.screen_name
						from_user = status.author.name
						to_user_id = me.screen_name
						to_user = me.name
						location_me = me.location
						location_bully = status.user.location
						time_now = status.created_at
						details_object = {'from_user':from_user,
										'to_user':to_user,
										'title':tweet,
										'completed':location_bully,
										'bully_rate':prediction,
										'platform':'twitter',
										'time_now':time_now}
						email_object = {'from_user':from_user,
										'from_user_id':from_user_id,
										'to_user':to_user,
										'to_user_id':to_user_id,
										'bully_tweet':tweet,
										'location_bully':location_bully,
										'location_me':location_me,
										'bully_rate':prediction,
										'time_now':time_now,
										'to':'pratikbansode2@gmail.com'}
						requests.post(url = url, data = details_object)
						requests.post(url = email_url,data = email_object)
						#api.update_status("@" + status.author.screen_name+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)",in_reply_to_status_id= tweet_id)
					else:
						print ("not bullying")
						#print(tweet)
						#api.update_status("@" + status.author.screen_name+"\n Good job, you're not a bully! (I am a bot in testing, don't take this too seriously)", in_reply_to_status_id= tweet_id)

				print('Thread Destroyed')

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

		return render(request, 'success.html')
	else:
		return render(request, 'hashtag.html')

def profile(request):
	

	def call(tweet):
		resp = requests.get('https://elit-hack.herokuapp.com/?query='+tweet)
		prediction = float(resp.text)


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


	for status in tweepy.Cursor(api.home_timeline,exclude_replies=True).items(5):
		#print ("tweet: "+ status.text.encode('utf-8'))
		# get rid of punctuation
		tweet_id = status.id
		tweet = status.text
		tweet = tweet.lower()
		prediction = call(tweet)
		me = api.me()
		url = 'https://cyber-bullying-report.herokuapp.com/api/task-create/'
		email_url ='http://cyber-bullying-report.herokuapp.com/api/sendmail/1'
		if prediction>0.5:
			print ("bullying")
			print (tweet)
			from_user_id = status.author.screen_name
			from_user = status.author.name
			to_user_id = me.screen_name
			to_user = me.name
			location_me = me.location
			location_bully = status.user.location
			time_now = status.created_at
			details_object = {'from_user':from_user,
							'to_user':to_user,
							'title':tweet,
							'completed':location_bully,
							'bully_rate':prediction,
							'platform':'twitter',
							'time_now':time_now}
			email_object = {'from_user':from_user,
							'from_user_id':from_user_id,
							'to_user':to_user,
							'to_user_id':to_user_id,
							'bully_tweet':tweet,
							'location_bully':location_bully,
							'location_me':location_me,
							'bully_rate':prediction,
							'time_now':time_now,
							'to':'pratikbansode2@gmail.com'}
			requests.post(url = url, data = details_object)
			requests.post(url = email_url,data = email_object)
			#api.update_status("@" + status.author.screen_name+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)",in_reply_to_status_id= tweet_id)
		else:
			print ("not bullying")
			print(tweet)
			#api.update_status("@" + status.author.screen_name+"\n Good job, you're not a bully! (I am a bot in testing, don't take this too seriously)", in_reply_to_status_id= tweet_id)

	return redirect("https://twitter.com/MayurDarkunde2")



def homeView(request):
	return render(request, 'main.html')



def contact_page(request):    
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		mess = request.POST['message']
		msg = Admin_Messages(name=name,email=email,message=mess)
		msg.save()
		return redirect('/#three')
	else:    
		return render(request, '/#three')

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)




@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')


@api_view(['POST'])
def sendMail(request, pk):	

	# parse json data:
	json_object = json.dumps(request.data)   
	y = json.loads(json_object)

	# print(y['message'])
		
	subject = "Bullying of <userid> <username>"
	subject = "Bullying of "+ y['to_user_id'] + " "+ y['to_user']    
	message = "Hello sir/ma'am, \nThis is auto generated mail from bullied tweet. Details of victim and abuser is as follows.\nTake the necessary actions. \n"+  y['to_user']+ " and "+ y['location_me']+  ":" + "\nVictim's tweet: [message]. \nAbuser's username and location: "+ y['from_user']+" and "+ y['location_bully']+  "\nAbuser's tweet: "+  y['bully_tweet']+ "\nThanks and regards, \nTeam Elite"
	to = ['pranaykatariya1@gmail.com']
   	
	to[0] = y['to']
	msg = EmailMessage(subject=subject, body=message, from_email= settings.EMAIL_HOST_USER, to= to)
	        
	try:
		msg.send()
		return Response('Mail sent succsesfully!')
	except :
		return Response('Mail failed to send')	