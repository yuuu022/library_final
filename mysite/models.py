from typing import Any
from django.db import models

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