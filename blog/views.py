from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Comment
from .forms import AddPostForm, UpdatePostForm, CommentForm


# Create your views here.
class PostView(ListView):
	model = Post
	template_name = 'blog/post_index.html'

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class AddPostView(CreateView):
	model = Post
	form_class = AddPostForm
	template_name = 'blog/post_add.html'

class UpdatePostView(UpdateView):
	model = Post 
	form_class = UpdatePostForm
	template_name = 'blog/post_update.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('post_index')

class AddCommentView(CreateView):
	model = Comment
	template_name = 'blog/add_comment.html'
	form_class = CommentForm

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)
	success_url = reverse_lazy('comment_added')

class CommentAddedView(TemplateView):
	template_name = 'blog/comment_added.html'