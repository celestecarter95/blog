from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views
from models import Comment, Post, Category

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name='comment'),
	#url(r'^blogging/$', views.blogging, name='blogging'),
	url(r'^blogging/$', views.PostImageView.as_view(), name='blogging'),
	#url(r'^blog/$', views.blog, name='blog'),
	url(r'^category/$', views.CategoryView.as_view(), name='category'),
	url(r'^category/newCategory$', views.new_category, name='newCategory'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.DetailCategoryView.as_view(), name='detailCategory'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
