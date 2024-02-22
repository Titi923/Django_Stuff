from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='acasa'),
    path('admin/', views.admin, name='admin'),
    path('logare/', views.logare_user, name='logare'),
    path('delogare/', views.delogare_user, name='delogare'),
    path('register/', views.register_user, name='register'),
]
