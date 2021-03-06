from django.shortcuts import * 
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .forms import BlogPostForm #, BlogForm
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

class CategoryView(generic.ListView):
	model = Category
	template_name = 'blogapp/category_list.html'

class DetailCategoryView(generic.ListView):
	model = Category
	template_name = 'blogapp/category_detail.html'
	
	def get_queryset(self):
		category_id = self.kwargs['pk']
		print category_id 
		return Category.objects.filter(id=category_id)

def comment(request, post_id):
	p = get_object_or_404(Post, pk=post_id)
	try:
		comment_person= request.POST['person']
		blog_comment = request.POST['comment']
		print comment_person, blog_comment
	except (KeyError, Comment.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'blogapp/detail.html', {
			'post': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		newComment = Comment(person=comment_person, comment_text=blog_comment, post=p)
		newComment.save()
		return HttpResponseRedirect(reverse('blogapp:detail', args=(p.id,)))

class PostImageView(generic.FormView):
	template_name = 'blogapp/blogging.html'
	form_class = BlogPostForm

	def form_valid(self, form):
		
		#Grabbing all form fields and making an instance of Post
		new_title = form.cleaned_data['title']
		new_body = form.cleaned_data['body']
		new_poster = form.cleaned_data['blog_poster']
		new_date = form.cleaned_data['pub_date']
		new_keywords = form.cleaned_data['keywords']
		newPost = Post(title=new_title, body=new_body, blog_poster=new_poster, pub_date=new_date, keywords=new_keywords)
		newPost.picture = self.get_form_kwargs().get('files')['picture']
		newPost.save()

		#Adding all categoryies to newPost
		new_categories = form.cleaned_data['category']
		for category in new_categories:
			newPost.category.add(category)
		self.id = newPost.id

		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('blogapp:detail', kwargs={'pk': self.id})

def new_category(request):
	try:
		newCategory = Category(category_name = request.POST['category_name'])
		newCategory.save()
	except (KeyError, Category.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'blogapp/category_list.html')
	else:
		return HttpResponseRedirect(reverse('blogapp:category'))

#No model view form
#def blogging(request):
#	if request.method == 'POST':
#		form = BlogPostForm(request.POST, request.FILES)
#		print "Finding if form is valid"
#
#		if(form.is_valid()):
#			print "It's valid"
#			print(request.POST['title'])
#			print(request.POST['body'])
#			print(request.POST['pub_date'])
#			print(request.POST['blog_poster'])
#			print(request.POST['keywords'])
#			print(request.POST['category'])
#			
#			new_title = request.POST['title']
#			new_body = request.POST['body']
#			new_poster = request.POST['blog_poster']
#			new_date = request.POST['pub_date']
#			new_keywords = request.POST['keywords']
#			new_category = request.POST['category']
#			newPost = Post(title=new_title, body=new_body, blog_poster=new_poster, pub_date=new_date, keywords=new_keywords, picture=self.get_form_kwargs().get('files')['picture'])
#			newPost.save()
#
#			return HttpResponseRedirect(reverse('blogapp:index'))
#	return render_to_response('blogapp/blogging.html', {'form': BlogPostForm()}, context_instance=RequestContext(request))

#form.form and not model form
#def blog(request):
#	if request.method == 'POST':
#		form = BlogForm(request.POST)
#		if form.is_valid():
#			return HttpResponseRedirect('/index/')
#	else:
#		form = BlogForm()
#		return render(request, 'blogapp/blog.html', {'form': form})
