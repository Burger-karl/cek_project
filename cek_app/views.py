from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from contact.forms import ContactForm

# Create your views here.

class HomeView(TemplateView):
    """Renders the homepage of the application."""
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add SEO-friendly metadata or extra data if needed
        context["page_title"] = _("Welcome to Cek Project")
        context["meta_description"] = _("Cek Project is your trusted platform for ...")
        context['contact_form'] = ContactForm()
        return context


class AboutView(TemplateView):
    """Renders the About Us page of the application."""
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = _("About Us - Cek Project")
        context["meta_description"] = _("Learn more about our mission, vision, and team at Cek Project.")
        return context
    

class TeamView(TemplateView):
    """Renders the Team page of the application."""
    template_name = "team.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = _("Our Team - Cek Project")
        context["meta_description"] = _("Learn more about our partners, professionals, and team at CEK Project.")
        return context
 

from django.contrib.auth.views import LoginView


class AdminLoginView(LoginView):
    template_name = 'auth/login.html'
