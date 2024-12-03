# app01 urls
from django.urls import path,re_path
from web.views import account


urlpatterns = [
    path('register/', account.register, name='register'),
]