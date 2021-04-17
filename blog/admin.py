from django.contrib import admin
from .models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'slug', 'date_written')
	prepopulated_fields = {'slug' : ('title',)}

admin.site.site_header = 'Fond Figure Admin'
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('date_commented', 'post', 'commenter_name', 'commenter_email', 'commenter_comment',)
	list_filter = ('date_commented',)
	search_field = ('commenter_name', 'comment_email', 'commenter_comment')
	#actions = ['approve_comments']

	#def approve_comments(self, request, queryset):
		#queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)