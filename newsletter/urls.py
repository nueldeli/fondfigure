from django.urls import path
from .views import SubscriptionDoneView

urlpatterns = [
	path('subscription_done/', SubscriptionDoneView.as_view(), name='subscription_done'),
]