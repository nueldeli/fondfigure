from django import forms
from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _

class SignUpForm(forms.ModelForm):
	class Meta:
		model = User 
		fields = ('first_name', 'last_name', 'username', 'email', 'password')

		widgets = {
			'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}),
			'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}),
			'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
			'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
		}

		labels = {
			'first_name':_(''),
			'last_name':_(''),
			'username':_(''),
			'email':_(''),
			'password':_('')
		}

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user