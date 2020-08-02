from rest_framework import serializers
from .models import Task, Report, AadharCard, Image, Web, Video

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'


class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields ='__all__'


class AadharSerializer(serializers.ModelSerializer):
	class Meta:
		model = AadharCard
		fields ='__all__'

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields ='__all__'


class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields ='__all__'


class WebSerializer(serializers.ModelSerializer):
	class Meta:
		model = Web
		fields ='__all__'
