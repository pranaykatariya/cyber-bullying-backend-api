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