from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("Resume", views.resume, name = 'Resume'),
    path("Projects", views.project, name = 'Projects'),
    path("Contact", views.contact, name = 'Contact'),
    path("Search", views.search, name = 'search')
]