from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('experiences', views.index, name="experiences"),
    path('contact', views.contact, name="contact"),
    path('hobby', views.hobby, name="hobby"),
]