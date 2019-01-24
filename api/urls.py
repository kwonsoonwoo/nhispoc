from django.urls import path

from . import views

urlpatterns = [
    path('', views.data_list, name='data-list'),
    path('create/', views.data_create, name='data-create'),
]