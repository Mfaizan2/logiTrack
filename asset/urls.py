from django.urls import path
from . import views
urlpatterns = [
    path('', views.asset_list, name = 'asset_list'),
    path('create/', views.asset_create, name = 'asset_create'),
]
