from django import forms
from .models import Subscription
from django.utils.translation import gettext_lazy as _

class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		fields = ('email',)

		widgets = {
			'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
		}

		labels = {
			'email':_('')
		}