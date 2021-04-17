from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.views.generic import TemplateView, CreateView

# Create your views here.
class SendMessageView(CreateView):
	model = Message
	form_class = MessageForm
	template_name = 'contact/send_message.html'

class MessageSentView(TemplateView):
	template_name = 'contact/message_sent.html'