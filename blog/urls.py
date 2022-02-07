from django.urls import path
from .views import PostView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView, CommentAddedView

urlpatterns = [
	path('post_index/', PostView.as_view(), name='post_index'),
	path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
	path('add_post/', AddPostView.as_view(), name='post_add'),
	path('update_post/<int:pk>', UpdatePostView.as_view(), name='post_update'),
	path('delete_post/<int:pk>', DeletePostView.as_view(), name='post_delete'),
	path('add_comment/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
	path('comment_added/', CommentAddedView.as_view(), name='comment_added'),
]