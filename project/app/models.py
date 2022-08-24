from email.policy import default
from tkinter import Widget
from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import User_manager
choice = (
    ('user','user'),
    ('admin','admin')
)

class Creators(AbstractUser):
    username = None
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=150, null=True, unique=True)
    password = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    type = models.CharField(choices=choice, max_length=50, default='user')
    objects = User_manager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    class Meta:
        ordering =['-id',]
    
    def __str__(self):
        return self.fullname
    
class Subject(models.Model):
    title = models.CharField(max_length=150)
    writer = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        ordering=['-id',]
    
    def __str__(self):
        return self.title
    
class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sub')
    chaptername = models.CharField(max_length=150)
    pagenumber = models.IntegerField()
    writername = models.CharField(max_length=150)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.chaptername

class SubChapter(models.Model):  
    chapter = models.ForeignKey(Chapter, on_delete= models.CASCADE, related_name= 'chapter') 
    subchaptername = models.CharField(max_length=150)
    writername = models.CharField(max_length=150)
    pagenumber = models.IntegerField()

    class Meta:
        ordering = ['-id',]

    def __str__(self) :
        return self.subchaptername
