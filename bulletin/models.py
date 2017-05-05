from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Notice(models.Model):
    upload = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=40)
    content = models.CharField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    expiry_date =  models.DateTimeField('expiry date')
    def __str__(self):              # __unicode__ on Python 2
        return self.subject

 
class Student(models.Model):
    user = models.OneToOneField(User)
    branch =  models.CharField(max_length=40)
    enr_no = models.IntegerField(default=0)
    def __str__(self):  
          return "%s's profile" % self.user

class Category(models.Model):
    name = models.CharField(max_length=40)
    suscriber = models.ManyToManyField(Student, through='Subscription')
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Subscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subs_since = models.DateTimeField(auto_now=True)

class SNlink(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    star  = models.BooleanField()
    read  = models.BooleanField()

class CNlink(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
