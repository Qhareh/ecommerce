from django.urls import path
from .views import home,contact,about
urlpatterns = [
    path('',home, name="name"),
    path('contact',contact, name="contact"),
    path('about',about, name="about"),
  ]