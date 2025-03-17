from django.urls import path
from . import views

urlpatterns = [
    path('', views.sitee_list, name= 'sitee_list'),
    path('create/', views.sitee_create, name = 'sitee_create')
]
