from django.urls import path
from .views import SendMessageView, MessageSentView

urlpatterns = [
	path('send_message/', SendMessageView.as_view(), name='send_message'),
	path('message_sent/', MessageSentView.as_view(), name='message_sent'),
]