from django.db import models
from django.urls import reverse

# Create your models here.
class Subscription(models.Model):
	email = models.EmailField(max_length=200, unique=True)
	date_joined = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_joined']

	def __str__(self):
		return self.email + ' | ' + str(self.date_joined)

	def get_absolute_url(self):
		return reverse('subscription_done')