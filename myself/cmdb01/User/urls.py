#coding:utf-8
from django.conf.urls import include, url
import views
urlpatterns = [
    url(r'^phone_valid/$', views.phone_valid),
    url(r'^username_valid/$', views.username_valid),
    url(r'^register/$', views.register),
]