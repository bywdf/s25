
# app01 urls
from django.urls import path, include
from app01 import views


urlpatterns = [
    path('send/sms/', views.send_sms),
    path('register/', views.register),
]