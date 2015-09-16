from django.shortcuts import render
from django.views import generic

from .models import Post, Comment, Category

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world")

class IndexView(generic.ListView):
	model = Post
	template_name = 'blogapp/index.html'

class DetailView(generic.DetailView):
	model = Post
	template_name = 'blogapp/detail.html'
