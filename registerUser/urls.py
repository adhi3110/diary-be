from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('hello/', views.HelloView.as_view(), name='hello'),
]