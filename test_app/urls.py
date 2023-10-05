from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home1'),
    path('2/', views.home2, name='home2'),
    path('3/', views.home3, name='home3'),
]