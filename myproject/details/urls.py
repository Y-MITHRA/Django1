from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_detail, name='add_detail'),
    path('', views.detail_list, name='detail_list'),
]
