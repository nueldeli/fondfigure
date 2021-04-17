from django.db import models
from django.urls import reverse

# Create your models here.
class Message(models.Model):
	date_sent = models.DateTimeField(auto_now_add=True)
	sender_name = models.CharField(max_length=200)
	sender_email = models.EmailField(max_length=200)
	sender_message = models.TextField()

	class Meta:
		ordering = ['-date_sent']

	def __str__(self):
		return self.sender_name + ' | ' + str(self.date_sent)

	def get_absolute_url(self):
		return reverse('message_sent')

