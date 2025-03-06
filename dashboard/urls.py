from django.urls import path
from . import views
app_name = "dashboard"
urlspattern = [
    path("", views.dashboard)
]