from django.shortcuts import render
from django.views import generic

from .models import Post, Comment, Category

from django.http import HttpResponse

class IndexView(generic.ListView):
	model = Post
	template_name = 'blogapp/index.html'

	def get_queryset(self):
		# SELECT * from blogapp_post ORDER BY pub_date DESC LIMIT 10
		return Post.objects.order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
	model = Post
	template_name = 'blogapp/detail.html'
