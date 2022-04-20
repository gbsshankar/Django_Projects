from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns=[path('Login/',views.Login,name='Login'),
             path('Login/output',views.output,name='output'),
             ]