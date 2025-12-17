from django.urls import path
from .views import HomeView, AboutView, AdminLoginView, TeamView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', AdminLoginView.as_view(), name='login'),
    path('team/', TeamView.as_view(), name='team'),
]