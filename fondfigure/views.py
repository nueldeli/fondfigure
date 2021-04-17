from django.views.generic import CreateView, TemplateView
from blog.models import Post
from newsletter.forms import SubscriptionForm

class HomeView(CreateView):
	template_name = 'home.html'
	form_class = SubscriptionForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['latest_post'] = Post.objects.all()[:]
		return context

class AboutView(TemplateView):
	template_name = 'about.html'