from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Category

#class CommentInline(admin.TabularInline):
#	model = Comment
#	extra = 3

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'keywords', 'pub_date']
#	inlines = [CommentInline]
	list_filter = ['pub_date']
	search_field = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
