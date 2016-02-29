from django.db import models
from django.contrib import admin

# Create your models here.

class BlogsPost(models.Model):
	#define the title and its length, body no limitation, timestamp
	title = models.CharField(max_length = 150)
	body = models.TextField()
	timestamp = models.DateTimeField()

admin.site.register(BlogsPost)