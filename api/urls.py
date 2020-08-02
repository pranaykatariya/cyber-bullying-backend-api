from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

	path('', views.apiOverview, name="api-overview"),

	#Task api
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', csrf_exempt(views.taskCreate), name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),


	#Report Api
	path('report-list/', views.reportList, name="report-list"),
	path('report-detail/<str:pk>/', views.reportDetail, name="report-detail"),
	path('report-create/', csrf_exempt(views.reportCreate), name="report-create"),

	path('report-update/<str:pk>/', views.reportUpdate, name="report-update"),
	path('report-delete/<str:pk>/', views.reportDelete, name="report-delete"),


	#aadhar api
	path('aadhar-list/', views.aadharList, name="aadhar-list"),
	path('aadhar-detail/<str:pk>/', views.aadharDetail, name="aadhar-detail"),
	path('aadhar-create/', csrf_exempt(views.aadharCreate), name="aadhar-create"),

	path('aadhar-update/<str:pk>/', views.aadharUpdate, name="aadhar-update"),
	path('aadhar-delete/<str:pk>/', views.aadharDelete, name="aadhar-delete"),


	#image api
	path('image-list/', views.imageList, name="image-list"),
	path('image-detail/<str:pk>/', views.imageDetail, name="image-detail"),
	path('image-create/', csrf_exempt(views.imageCreate), name="image-create"),

	path('image-update/<str:pk>/', views.imageUpdate, name="image-update"),
	path('image-delete/<str:pk>/', views.imageDelete, name="image-delete"),


	#video api
	path('video-list/', views.videoList, name="video-list"),
	path('video-detail/<str:pk>/', views.videoDetail, name="video-detail"),
	path('video-create/', csrf_exempt(views.videoCreate), name="video-create"),

	path('video-update/<str:pk>/', views.videoUpdate, name="video-update"),
	path('video-delete/<str:pk>/', views.videoDelete, name="video-delete"),



	#web api
	path('web-list/', views.webList, name="web-list"),
	path('web-detail/<str:pk>/', views.webDetail, name="web-detail"),
	path('web-create/', csrf_exempt(views.webCreate), name="web-create"),

	path('web-update/<str:pk>/', views.webUpdate, name="web-update"),
	path('web-delete/<str:pk>/', views.webDelete, name="web-delete"),

	#email api
	path('sendmail/<str:pk>', views.sendMail, name='sendmail'),
]
