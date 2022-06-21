
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author= models.ForeignKey(User, on_delete=models.CASCADE, default='Anonymous')
    Created_date= models.DateTimeField(auto_now_add=True)
    Published_date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title