from django.contrib import admin
from .models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
	list_display = ('sender_name', 'sender_email', 'date_sent', 'sender_message')

admin.site.register(Message, MessageAdmin)