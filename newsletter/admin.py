from django.contrib import admin
from .models import Subscription

# Register your models here.
class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('email', 'date_joined')

admin.site.register(Subscription, SubscriptionAdmin)