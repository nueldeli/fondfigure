from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm

# Create your views here.
class SignUpView(CreateView):
	form_class = SignUpForm
	template_name = 'registration/signup.html'
	success_url = reverse_lazy('login')

def user_profile(request):
	return render(request, 'registration/user_profile.html')