from django import forms
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'slug', 'thumbnail_img', 'post_snippet', 'content')

		widgets = {
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post title'}),
			'slug':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Slug is automatically generated. It is OK to leave it empty'}),
			'thumbnail_img':forms.FileInput(),
			'post_snippet':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Brief extract, not more than 250 characters'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing'})
		}

		labels = {
			'author':_(''),
			'title':_(''),
			'slug':_(''),
			'post_snippet':_(''),
			'content':_('')
		}

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'slug', 'thumbnail_img', 'post_snippet', 'content')

		widgets = {
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post title'}),
			'slug':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Slug is automatically generated. It is OK to leave it empty'}),
			'thumbnail_img':forms.FileInput(),
			'post_snippet':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Brief extract, not more than 250 characters'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing'})
		}

		labels = {
			'author':_(''),
			'title':_(''),
			'slug':_(''),
			'thumbnail_img':_(''),
			'post_snippet':_(''),
			'content':_('')
		}



class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('commenter_name', 'commenter_email', 'commenter_comment')

		widgets = {
			'commenter_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
			'commenter_email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'commenter_comment':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type your comment here...'})
		}

		labels = {
			'commenter_name':_(''),
			'commenter_email':_(''),
			'commenter_comment':_('')
		}

