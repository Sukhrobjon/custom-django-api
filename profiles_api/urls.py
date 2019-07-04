from django.conf.urls import url, include

from rest_framework import routers

from profiles_api import views


urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),

]
