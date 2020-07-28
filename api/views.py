from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.conf import settings

import json
# Create your views here.

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

	print(y['message'])
		
	subject = "Bullying of <userid> <username>"    
	message = "Hello sir/ma'am, \nThis is auto generated mail from bullied tweet. Details of victim and abuser is as follows.\nTake the necessary actions. \nVictim username and location: \nVictim's tweet: [message]. \nAbuser's username and location: [username and location] \n Abuser's tweet: [abuser message] \n Thanks and regards, \nTeam Elite"
	to = ['pranaykatariya1@gmail.com']
   	
	to[0] = y['to']
	msg = EmailMessage(subject=subject, body=message, from_email= settings.EMAIL_HOST_USER, to= to)
	        
	try:
		msg.send()
		return Response('Mail sent succsesfully!')
	except :
		return Response('Mail failed to send')	