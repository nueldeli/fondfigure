from django.urls import path
from .views import PostView, PostDetailView, AddCommentView, CommentAddedView

urlpatterns = [
	path('post_index/', PostView.as_view(), name='post_index'),
	path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
	path('add_comment/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
	path('comment_added/', CommentAddedView.as_view(), name='comment_added'),
]