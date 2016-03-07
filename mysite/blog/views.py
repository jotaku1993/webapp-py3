#coding=utf-8
from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
	#obtain all the blogpost objects from database
	blog_list = BlogsPost.objects.all()
	#return the index and connect them with "posts"
	return render_to_response('index.html', {'posts':blog_list} )