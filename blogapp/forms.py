from django import forms
from django.forms import ModelForm

from .models import Post

class CommentForm(forms.Form):
	person = forms.CharField(max_length=200)
	comment = forms.CharField(widget=forms.Textarea, max_length=200)

class BlogPostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['active']
		labels = {
			'pub_date': ('Publishing'),
			'blog_poster': ('Name'),
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'pub_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
			'blog_poster': forms.TextInput(attrs={'class': 'form-control'}),
			'keywords': forms.TextInput(attrs={'class': 'form-control'}),
			'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}

#class BlogForm(forms.Form):
#	title = forms.CharField(max_length=200)
#	body = forms.CharField(widget=forms.Textarea)
#	pub_date = forms.DateTimeField()
#	blog_poster = forms.CharField(max_length=200)
#	keywords = forms.CharField(max_length=200)
