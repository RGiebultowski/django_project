from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='login_system-home'),
    path('about/', views.about, name='login_system-about'),
]
