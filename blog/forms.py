from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _

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

