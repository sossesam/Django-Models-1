
from django.db import models


# Create your models here.
class Author:
    userName=models.CharField(max_length=50)


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
  
    Created_date= models.DateTimeField(auto_now_add=True)
    Published_date= models.DateTimeField(auto_now_add=True)