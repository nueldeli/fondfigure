from django import forms
from .models import Message
from django.utils.translation import gettext_lazy as _

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('sender_name', 'sender_email', 'sender_message')

		widgets = {
			'sender_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
			'sender_email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'sender_message':forms.Textarea(attrs={'class':'form-cotrnol w-100', 'placeholder':'Type message...'}),
		}

		labels = {
			'sender_name':_(''),
			'sender_email':_(''),
			'sender_message':_(''),
		}