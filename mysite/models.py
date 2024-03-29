from typing import Any
from django.db import models
from django import forms

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Postdetail(models.Model):
    state=(
        ("館藏中","館藏中"),
        ("預約中","預約中"),
        ("借出中","借出中"),
    )
    Bookname = models.CharField(max_length=200)
    Author = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    Content = models.TextField()
    Publiccationdate = models.CharField(max_length=20)
    State = models.CharField(max_length=8,choices=state)
    enable = models.BooleanField(default=True)

    
    def __str__(self):
        return self.Bookname
    
class PostdetailTwo(models.Model):
    state=(
        ("館藏中","館藏中"),
        ("預約中","預約中"),
        ("借出中","借出中"),
    )
    Bookname = models.CharField(max_length=200)
    Author = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    Content = models.TextField()
    Publiccationdate = models.CharField(max_length=20)
    State = models.CharField(max_length=8,choices=state)
    Img = models.TextField() 
    
    def __str__(self):
        return self.Bookname

class User(models.Model):
    user_id = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=50)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id
    
class Book(models.Model):
    state = (
        ("館藏中","館藏中"),
        ("預約中","預約中"),
        ("借出中","借出中"),
    )
    title = models.CharField(max_length=100)  
    state = models.CharField(max_length=8, choices=state)  
    Author = models.CharField(max_length=100) 