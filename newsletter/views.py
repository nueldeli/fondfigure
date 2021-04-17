from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SubscriptionDoneView(TemplateView):
	template_name = 'newsletter/subscription_done.html'