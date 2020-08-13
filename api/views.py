from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, ReportSerializer, AadharSerializer, ImageSerializer, WebSerializer, VideoSerializer

from .models import Task, Admin_Messages, Report, AadharCard, Image, Video, Web

from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.conf import settings

import tweepy
import threading
import time
from tweepy import OAuthHandler
import requests


from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import get_template

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
										lang="en").items(5):
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
					requests.post(url = email_url,data = email_object)
					#api.update_status("@" + status.author.screen_name+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)",in_reply_to_status_id= tweet_id)
				else:
					print ("not bullying")
					print(tweet)
					#api.update_status("@" + status.author.screen_name+"\n Good job, you're not a bully! (I am a bot in testing, don't take this too seriously)", in_reply_to_status_id= tweet_id)
			print('Thread destroyed')

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

	
	return redirect("https://twitter.com/MayurDarkunde2")



def homeView(request):

	if request.user.is_authenticated:
		print('pranay')
		ctx ={
        	'data' : 'pranay',
    	}
	else:
		print('noone')
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
		#task list
		'Task List':'/task-list/',
		'Task Detail View':'/task-detail/<str:pk>/',
		'Task Create':'/task-create/',
		'Task Update':'/task-update/<str:pk>/',
		'Task Delete':'/task-delete/<str:pk>/',

		#report list
		'Report List':'/report-list/',
		'Report Detail View':'/report-detail/<str:pk>/',
		'Report Create':'/report-create/',
		'Report Update':'/report-update/<str:pk>/',
		'Report Delete':'/report-delete/<str:pk>/',

		
		#aadhar list
		'Aadhar List':'/aadhar-list/',
		'Aadhar Detail View':'/aadhar-detail/<str:pk>/',
		'Aadhar Create':'/aadhar-create/',
		'Aadhar Update':'/aadhar-update/<str:pk>/',
		'Aadhar Delete':'/aadhar-delete/<str:pk>/',



		#Image list
		'image List':'/image-list/',
		'image Detail View':'/image-detail/<str:pk>/',
		'image Create':'/image-create/',
		'image Update':'/image-update/<str:pk>/',
		'image Delete':'/image-delete/<str:pk>/',


		
		#video list
		'video List':'/video-list/',
		'video Detail View':'/video-detail/<str:pk>/',
		'video Create':'/video-create/',
		'video Update':'/video-update/<str:pk>/',
		'video Delete':'/video-delete/<str:pk>/',
	
		
		#web list
		'web List':'/web-list/',
		'web Detail View':'/web-detail/<str:pk>/',
		'web Create':'/web-create/',
		'web Update':'/web-update/<str:pk>/',
		'web Delete':'/web-delete/<str:pk>/',

		}

	return Response(api_urls)


#Task api code

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
    
    # Add email data
    data = ['pranaykatariya1@gmail.com','ajaychordiya24@gmail.com', 'vishalpatil7860@gmail.com']

    # code for uploading email data to database server
    # for i in data:
    #     obj = Promotion_Email_List(email= i)
        
    #     try:
    #         obj.save()
    #         print(i)
    #     except:
    #         print("Exception occured: "+i)

    json_object = json.dumps(request.data)
    y = json.loads(json_object)
    
    data = y['email']
    print('data')
    print(data)


    # send email code
    subject = "Monetize Your B.E. Projects !!"    
    message = get_template('promotionformat.html').render()
    to = ['pranaykatariya1@gmail.com']
    pass_counter = 0
    fail_counter = 0
    for x in data[:400]:
        print(x)
        to[0] = x
        msg = EmailMessage(subject=subject, body=message, from_email= settings.EMAIL_HOST_USER, to= to)
        msg.content_subtype = 'html'
        
        try:
            msg.send()
            pass_counter+=1
            # Promotion_Email_List.objects.filter(email=x.email).update(sent=True)
            print("Mail sent to "+ x)
            print(pass_counter+fail_counter)
        except:
            fail_counter+=1
            print("Mail failed: "+ x)
    
    

    print("Email sending job end here is your task summarry:")
    print("Successfully sent: "+str(pass_counter))
    print("sending failed: "+str(fail_counter))
    
            
    ctx ={    
        # 'authorization' : authorization,
        # 'result': result
    }

    return Response('Successfully sent '+str(pass_counter))
    



# @api_view(['POST'])
# def sendMail(request, pk):	

# 	# parse json data:
# 	json_object = json.dumps(request.data)   
# 	y = json.loads(json_object)

# 	# print(y['message'])
# 	if y['to_user_id'] is None:
# 		y['to_user_id'] = " "
	
# 	if y['to_user'] is None:
# 		y['to_user'] = " "
	
# 	str1 = ""
# 	str2 = ""
    
#     # traverse in the string   
    
# 	for ele in y['to_user_id']: 
    	
# 		str1 += str(ele)
    
# 	for elem in y['to_user']:  
    	
# 		str2 += elem
    

# 	subject = "Bullying of <userid> <username>"
# 	# subject = "Bullying of "+ y['to_user_id'] + " "+ y['to_user']
	
# 	if len(str1.strip()) == 0:
# 		subject = "Bullying spotted"
# 	else:
# 		subject = "Bullying of "+ str1 + " "+ str2    
	
# 	message = "Hello sir/ma'am, \nThis is auto generated mail from bullied tweet. Details of victim and abuser is as follows.\nTake the necessary actions. \n"+  str2 + " and "+ y['location_me']+  ":" + "\nVictim's tweet: [message]. \nAbuser's username and location: "+ y['from_user']+" and "+ y['location_bully']+  "\nAbuser's tweet: "+  y['bully_tweet']+ "\nThanks and regards, \nTeam Elite"
# 	to = ['pranaykatariya1@gmail.com']
   	
# 	to[0] = y['to']
# 	msg = EmailMessage(subject=subject, body=message, from_email= settings.EMAIL_HOST_USER, to= to)
	        
# 	try:
# 		msg.send()
# 		return Response('Mail sent succsesfully!')
# 	except:
# 		return Response('Mail failed to send')	


#Report REST api's

@api_view(['GET'])
def reportList(request):
	reports = Report.objects.all().order_by('-complain_id')
	serializer = ReportSerializer(reports, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def reportDetail(request, pk):
	reports = Report.objects.get(complain_id=pk)
	serializer = ReportSerializer(reports, many=False)
	return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def reportCreate(request):
	serializer = ReportSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def reportUpdate(request, pk):
	report = Report.objects.get(complain_id=pk)
	serializer = ReportSerializer(instance=report, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def reportDelete(request, pk):
	report = Report.objects.get(complain_id=pk)
	task.delete()

	return Response('Item succsesfully delete!')




#Aadhar REST api's

@api_view(['GET'])
def aadharList(request):
	aadhar = AadharCard.objects.all()
	serializer = AadharSerializer(aadhar, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def aadharDetail(request, pk):
	aadhar = AadharCard.objects.get(aadharno=pk)
	serializer = AadharSerializer(aadhar, many=False)
	return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def aadharCreate(request):
	serializer = AadharSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def aadharUpdate(request, pk):
	aadhar = AadharCard.objects.get(aadharno=pk)
	serializer = AadharSerializer(instance=aadhar, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def aadharDelete(request, pk):
	aadhar = AadharCard.objects.get(aadharno=pk)
	aadhar.delete()

	return Response('Item succsesfully delete!')




#Image REST api's

@api_view(['GET'])
def imageList(request):
	image = Image.objects.all()
	serializer = ImageSerializer(image, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def imageDetail(request, pk):
	image = Image.objects.get(complain_id=pk)
	serializer = ImageSerializer(image, many=False)
	return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def imageCreate(request):
	serializer = ImageSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def imageUpdate(request, pk):
	image = Image.objects.get(complain_id=pk)
	serializer = ImageSerializer(instance=image, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def imageDelete(request, pk):
	image = Image.objects.get(complain_id=pk)
	image.delete()

	return Response('Item succsesfully delete!')



#Video REST api's

@api_view(['GET'])
def videoList(request):
	video = Video.objects.all()
	serializer = VideoSerializer(video, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def videoDetail(request, pk):
	video = Video.objects.get(complain_id=pk)
	serializer = VideoSerializer(video, many=False)
	return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def videoCreate(request):
	serializer = VideoSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def videoUpdate(request, pk):
	video = Video.objects.get(complain_id=pk)
	serializer = VideoSerializer(instance=video, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def videoDelete(request, pk):
	video = Video.objects.get(complain_id=pk)
	video.delete()

	return Response('Item succsesfully delete!')


#Web REST api's

@api_view(['GET'])
def webList(request):
	web = Web.objects.all()
	serializer = WebSerializer(web, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def webDetail(request, pk):
	web = Web.objects.get(complain_id=pk)
	serializer = WebSerializer(web, many=False)
	return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def webCreate(request):
	serializer = WebSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def webUpdate(request, pk):
	web = Web.objects.get(complain_id=pk)
	serializer = WebSerializer(instance=web, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def webDelete(request, pk):
	web = Web.objects.get(complain_id=pk)
	web.delete()

	return Response('Item succsesfully delete!')