from django.db import models

# Create your models here.

class Task(models.Model):
  from_user = models.CharField(max_length=200,null=True, blank=True)
  to_user = models.CharField(max_length=200, null=True, blank=True)
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
  bully_rate = models.FloatField()
  platform = models.CharField(max_length=200,null=True, blank=True)
  time_now = models.DateTimeField(auto_now_add=True)
 
      
  def __str__(self):
    return self.title


class Admin_Messages(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(null=False)
    message = models.TextField(null=True, blank=True)



class AadharCard(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64,null=True, blank=True)
    email = models.EmailField(null=False)
    aadharno = models.CharField(max_length=64)
    dob = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=64,null=True, blank=True)


class Report(models.Model):
  complain_id = models.AutoField(primary_key=True)
  complainer = models.CharField(max_length=64)
  victim = models.CharField(max_length=64)
  abuser = models.CharField(max_length=64)
  tweet = models.TextField(null=True, blank=True)
  completed = models.CharField(max_length=64)
  time_now = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
  complain_id = models.AutoField(primary_key=True)
  platform_id = models.CharField(max_length=64, null=True, blank=True)
  url = models.CharField(max_length=128)
  platform = models.CharField(max_length=64, null=True, blank=True)
  result = models.CharField(max_length=64, null=True, blank=True)
  time_now = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
  complain_id = models.AutoField(primary_key=True)
  platform_id = models.CharField(max_length=64, null=True, blank=True)
  url = models.CharField(max_length=128)
  platform = models.CharField(max_length=64, null=True, blank=True)
  result = models.CharField(max_length=64, null=True, blank=True)
  time_now = models.DateTimeField(auto_now_add=True)



class Web(models.Model):
  complain_id = models.AutoField(primary_key=True)
  url = models.CharField(max_length=128)
  result = models.CharField(max_length=64)
  time_now = models.DateTimeField(auto_now_add=True)
